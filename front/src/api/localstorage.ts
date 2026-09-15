import type { Rate } from "../types";

export function getSavedRatings(): Rate[] {
    let rawLocalStItem = localStorage.getItem("ratings");
    if (!rawLocalStItem) {
        return [];
    }
    else {
        return JSON.parse(rawLocalStItem);
    }

}

export function saveRatings(ratings: Rate[]) {
    localStorage.setItem("ratings", JSON.stringify(ratings));
}