class Influencer:
    def __init__(self, num_selfies, num_bio_links):
        self.num_selfies = num_selfies
        self.num_bio_links = num_bio_links

    def __repr__(self):
        return f"({self.num_selfies}, {self.num_bio_links})"


# dont touch above this line


def vanity(influencer):
    vanity = influencer.num_bio_links * 5 + influencer.num_selfies
    return vanity


def vanity_sort(influencers):
    return sorted(influencers, key=vanity)


if __name__ == "__main__":
    influencer = Influencer(10, 3)
    influencer2 = Influencer(4, 3)
    influencer3 = Influencer(23, 3)
    print(vanity(influencer))
    print(vanity_sort([influencer, influencer2, influencer3]))
