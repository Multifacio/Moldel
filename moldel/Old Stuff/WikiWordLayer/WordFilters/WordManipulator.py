class WordManipulator:
    @staticmethod
    def get_seasons(parsed_data):
        seasons = set()
        for candidate in parsed_data:
            seasons.add(parsed_data[candidate]["season"])
        return seasons

    @staticmethod
    def get_season_candidates(season, parsed_data):
        return [c for c in parsed_data if parsed_data[c]["season"] == season]

    @staticmethod
    def get_season_page_occurrence_word(word, season, parsed_data):
        season_candidates = WordManipulator.get_season_candidates(season, parsed_data)
        count = 0
        for c in season_candidates:
            if word in parsed_data[c]["occ"]:
                count += 1
        return count

    @staticmethod
    def get_total_occurrence_word(word, parsed_data):
        sum = 0
        for candidate in parsed_data:
            sum += parsed_data[candidate]["occ"].get(word, 0)
        return sum