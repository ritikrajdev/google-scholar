from requests import get
from bs4 import BeautifulSoup


class Scholar:
    def __init__(self, scholar_id) -> None:
        self.scholar_id = scholar_id
        self._get_details()


    def _get_details(self) -> None:
        uri = 'https://scholar.google.com/citations?user=' + self.scholar_id + '&pagesize=1000000000'
        response = get(uri)

        if response.status_code // 100 != 2:
            raise LookupError('No Such Scholar Exists')

        response = response.content
        soup = BeautifulSoup(response, 'html.parser')

        self.name = soup.find(id='gsc_prf_in').text
        
        self.data = {}

        for row in soup.findAll('tr', class_='gsc_a_tr'):
            paper_id = row.find('a', class_='gsc_a_at')['href'].split(':')[-1]

            citations = row.find('a', class_='gsc_a_ac gs_ibl').text
            year = row.find(class_='gsc_a_h gsc_a_hc gs_ibl').text

            if year and citations:
                year = int(year)
                citations = int(citations)
            else:
                continue

            self.data[paper_id] = {'citations': citations, 'year': year}

    def __str__(self):
        return str({
            'name': self.name,
            'data': self.data
        })


if __name__ == '__main__':
    print(Scholar(input('id: ')))

