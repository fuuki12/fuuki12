import requests

GENERATE_FILE_NAME = 'README.md'

url = "https://zenn.dev/api/articles?username=maple_siro&order=latest"


def fetch_data_from_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if request was successful
        return response.json()       # Convert to JSON
    except (requests.RequestException, ValueError) as err:
        print(f"Error while getting data from API - {err}")
        return None


def prepare_content(jsonData):
    # Guard clause instead of wrapping whole code in a condition
    if jsonData is None:
        return

    articles_list = [f"- [{article['title']}]({'https://zenn.dev/' + article['path']})"
                     for article in jsonData["articles"][:5]]

    formatted_articles_list = '\n'.join(articles_list)

    return '''
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

## 🎾 My Zenn Article

{zennArticle}
    '''.strip().format(zennArticle=formatted_articles_list)


def write_to_file(file_name, content):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(content)


jsonData = fetch_data_from_api(url)
content = prepare_content(jsonData)

if content:
    write_to_file(GENERATE_FILE_NAME, content)
