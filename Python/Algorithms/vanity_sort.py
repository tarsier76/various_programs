class Influencer:
    def __init__(self, num_selfies, num_bio_links):
        self.num_selfies = num_selfies
        self.num_bio_links = num_bio_links

    def __repr__(self):
        return f"({self.num_selfies}, {self.num_bio_links})"

def vanity(influencer):
    vanity = influencer.num_bio_links * 5 + influencer.num_selfies
    print(influencer)
    print(vanity)
    return vanity 

def vanity_sort(influencers):
    total_list = []
    for influencer in influencers:
        total_list.append(influencer)
    return sorted(total_list, key=vanity)

