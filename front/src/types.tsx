export type Page = "search" | "rated" | "recommendations" | "about";
export type PageContextType = { page: Page, setPage: (p: Page) => void };