import { ENDPOINT } from "../consts";
import { getSavedRatings } from "./localstorage";
import { ServerIsBusyError, type Movie, type Rate } from "../types";

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
            // 503 means that server is currently training model 
            if (servResponse.status == 503)
                throw new ServerIsBusyError();

            throw new Error(`Response status ${servResponse.status}`);
        }
    } catch (error) {
        console.error("Unexpected error in retrainNewModel().", error);
        throw error;
    }
}

export async function getRecommendations(modelName: string): Promise<Movie[]> {
    const URL = ENDPOINT + `/models/recommend/${modelName}`;
    try {
        const servResponse = await fetch(URL, { method: "POST" });
        if (!servResponse.ok) {
            throw new Error(`Response status ${servResponse.status}`);
        }

        return await servResponse.json();
    } catch (error) {
        console.error("Unexpected error in getRecommendations().", error);
        throw error;
    }
}

export async function trainingStatus(): Promise<string> {
    const URL = ENDPOINT + `/models/trainStatus`;
    try {
        const servResponse = await fetch(URL, { method: "GET" });
        if (!servResponse.ok) {
            throw new Error(`Response status ${servResponse.status}`);
        }

        return await servResponse.json();
    } catch (error) {
        console.error("Unexpected error in trainingStatus().", error);
        throw error;
    }
}