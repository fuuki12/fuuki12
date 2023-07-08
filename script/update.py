import requests

GENERATE_FILE_NAME = 'README.md'

url = "https://zenn.dev/api/articles?username=maple_siro&order=latest"


def get_data_from_api(url):
    try:
        res = requests.get(url)
        res.raise_for_status()  # Check if request was successful
        return res.json()       # Convert to JSON
    except (requests.RequestException, ValueError):
        print("Error while getting data from API")
        return None


def write_to_file(file_name, content):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(content)


jsonData = get_data_from_api(url)

if jsonData is not None:
    resultList = ["- [{}]({})".format(item['title'], item['path'])
                  for item in jsonData["articles"][:5]]
    resultList = '\n'.join(resultList)

    docs_str = '''
### Maple Profile 🍁

I am a frontend engineer specializing in Typescript and React. I enjoy thinking deeply about architecture.

## Used Languages

<p align="left">
    <a href="https://github.com/fuuki12" target="_blank">
    <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=fuuki12&layout=compact&bg_color=DEG,ffb3ba,ffdfba&title_color=fc85ae" width="500px;" target="_blank" />
    </a>
</p>

## 🔭 My Expertise

- Front end development with **TypeScript**, **React**.
- Frontend architecture, particularly for web applications.

## 🌱 What I'm currently learning

I'm currently deepening my understanding of efficient and scalable architecture designs.

## ✨ My Zenn Article

{zennArticle}
    '''.strip().format(zennArticle=resultList)

    write_to_file(GENERATE_FILE_NAME, docs_str)
