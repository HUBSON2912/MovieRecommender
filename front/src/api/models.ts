import { ENDPOINT } from "../consts";
import { getSavedRatings } from "./localstorage";
import type { Rate } from "../types";

export async function getModelsList(): Promise<string[]> {
    const URL = ENDPOINT + `/models/list`;
    try {
        const servResponse = await fetch(URL, { method: "POST" });
        if (!servResponse.ok) {
            throw new Error(`Response status ${servResponse.status}`);
        }

        return await servResponse.json();
    } catch (error) {
        console.error("Unexpected error in getModelsList().", error);
        throw error;
    }
}

export async function retrainNewModel() {
    const URL = ENDPOINT + `/models/retrain`;
    try {
        const userRatings: Rate[] = getSavedRatings();
        const servResponse = await fetch(URL, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(userRatings)
        });
        if (!servResponse.ok) {
            throw new Error(`Response status ${servResponse.status}`);
        }

        return await servResponse.json();
    } catch (error) {
        console.error("Unexpected error in retrainNewModel().", error);
        throw error;
    }
}