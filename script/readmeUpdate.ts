import axios from "axios";
import { Article } from "./model";

const api_key = "https://zenn.dev/";

const fetch = async <T>(path: string) => {
  const res = await fetch(`${api_key}api/${path}`);
  const result: T = await res.json();
  return result;
};

export const getStaticProps: any = async () => {
  const result = await fetch<{ articles: Article[] }>(
    "articles?username=maple_siro&order=latest"
  );
  console.log();

  return {
    props: {
      articles: result.articles,
    },
    revalidate: 60,
  };
};

// メインの関数
async function main() {}

main();
