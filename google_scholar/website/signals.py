from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Scholar, Paper
from .scholar import Scholar as _Scholar


@receiver(post_save, sender=Scholar)
def create_papers(sender: Scholar, instance: Scholar, created, **kwargs):
    if created:
        scholar = _Scholar(instance.id)

        instance.name = scholar.name
        instance.save()

        for paper_id, info in scholar.data.items():
            pre_existing_paper = Paper.objects.filter(id=paper_id)
            if not pre_existing_paper:
                citations = info['citations']
                year = info['year']
                instance.paper_set.create(id=paper_id, citation=citations, year=year)
            else:
                pre_existing_paper[0].scholars.add(instance)
