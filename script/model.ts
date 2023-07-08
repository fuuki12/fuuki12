export class User {
  id: number;
  username: string;
  name: string;
  avatar_small_url: string;

  constructor(
    id: number,
    username: string,
    name: string,
    avatar_small_url: string
  ) {
    this.id = id;
    this.username = username;
    this.name = name;
    this.avatar_small_url = avatar_small_url;
  }
}

class Publication {
  // Your properties for publication goes here.
  // It seems 'Publication' is 'null' always as per your provided JSON.
  // Please add appropriate fields once you have data for it.
}

export class Article {
  id: number;
  post_type: string;
  title: string;
  slug: string;
  comments_count: number;
  liked_count: number;
  body_letters_count: number;
  article_type: string;
  emoji: string;
  is_suspending_private: boolean;
  published_at: string;
  body_updated_at: string;
  source_repo_updated_at: string | null;
  pinned: boolean;
  path: string;
  user: User;
  publication: Publication | null;

  constructor(
    id: number,
    post_type: string,
    title: string,
    slug: string,
    comments_count: number,
    liked_count: number,
    body_letters_count: number,
    article_type: string,
    emoji: string,
    is_suspending_private: boolean,
    published_at: string,
    body_updated_at: string,
    source_repo_updated_at: string | null,
    pinned: boolean,
    path: string,
    user: User,
    publication: Publication | null
  ) {
    this.id = id;
    this.post_type = post_type;
    this.title = title;
    this.slug = slug;
    this.comments_count = comments_count;
    this.liked_count = liked_count;
    this.body_letters_count = body_letters_count;
    this.article_type = article_type;
    this.emoji = emoji;
    this.is_suspending_private = is_suspending_private;
    this.published_at = published_at;
    this.body_updated_at = body_updated_at;
    this.source_repo_updated_at = source_repo_updated_at;
    this.pinned = pinned;
    this.path = path;
    this.user = user;
    this.publication = publication;
  }
}
