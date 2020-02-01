from WikiWordLayer.DataExtractors.Jobs import Jobs
from WikiWordLayer.DataExtractors.DataExtractor import DataExtractor

class Job_Extractor(DataExtractor):
    """ The Job Extractor will convert candidates to a numberic vector where every number represents to which degree
    a candidate belongs to a job. The Job Extractor uses the Jobs enum for this which indicates which words belongs to
    which jobs. If a word belongs to n jobs then all n jobs will have their value increased by 1/n """

    def extract(self, parsed_data):
        words = set()
        word_jobs = dict()
        for j in Jobs:
            for w in j.value:
                words.add(w)
                word_jobs[w] = word_jobs.get(w, []) + [j]

        numberic_output = dict()
        for c in parsed_data:
            job_score = dict()
            for w in words:
                number = parsed_data[c]["occ"].get(w, 0)
                jobs = word_jobs[w]
                for j in jobs:
                    job_score[j] = (number / len(jobs)) + job_score.get(j, 0)
            numberic_output[c] = [job_score.get(j, 0) for j in Jobs]

        return numberic_output