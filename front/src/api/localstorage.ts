import type { Rate } from "../types";

export function getSavedRatings(): Rate[] {
    // todo tu jakieś problemy z typami
    let savedRatings: = localStorage.getItem("ratings");
    if (!savedRatings) {
        return [];
    }
    else {
        savedRatings = JSON.parse(savedRatings);
        if(!savedRatings)
            return [];
        return savedRatings.map((r: Rate) => r.movieId);
    }
    
}

export function saveRatings(ratings: Rate[]) {
    localStorage.setItem("ratings", JSON.stringify(ratings));
}