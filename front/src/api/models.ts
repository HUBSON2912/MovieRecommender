import { ENDPOINT } from "../consts";

export async function getModelsList(): Promise<string[]> {
    const URL = ENDPOINT + `/models/list`;
    try {
        const servResponse = await fetch(URL, { method: "POST" });
        if (!servResponse.ok) {
            throw new Error(`Response status ${servResponse.status}`);
        }

        return await servResponse.json();
    } catch (error) {
        console.error("Unexpected error in searchMovie().", error);
        throw error;
    }
}