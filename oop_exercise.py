class GenomicFeature():
    def __init__(self, chromosome, start, end, strand):
        self.chromosome = chromosome
        self.start = start
        self.end = end
        self.strand = strand

        if not isinstance(self.chromosome, str):
            raise ValueError ('Chromose is not string')
        if self.start > self.end:
            raise ValueError ('Start is shorter than end')
        elif self.start <= 0 or self.end <= 0:
            raise ValueError('Start and end must be greater than 0')
        if self.strand != '+' and self.strand != '-':
            raise ValueError ('Strand must be + or -')

    def length(self):
        return self.end - self.start + 1

    def overlaps(self, other):
        if self.chromosome != other.chromosome:
            return False
        if self.start <= other.end or self.end >= other.start:
            return True
        else:
            return False

    def describe(self):
        return f'type {type(self).__name__} Chromosone {self.chromosome} starts at {self.start} and ends at {self.end} with strand {self.strand}'

class Exon(GenomicFeature):
    def __init__(self, chromosone, start, end, strand, exon_number):
        self.exon_number = exon_number
        super().__init__(chromosone, start, end, strand)

    def describe(self):
        return f'{super().describe()} Exon number is {self.exon_number}'


#Task 3
class Gene(GenomicFeature):
    def __init__(self, chromosone, start, end, strand, name, self_exons):
        self_exons = []
        self.name = name
        self.self_exons = self_exons

    def add_exon(self, exon):
        self.self_exons = self.self_exons.append(exon)

    def total_exon_length(self):
        for exon in self.self_exons():

if __name__ == '__main__':
    a = GenomicFeature("chr1", 1000, 5000, "+")
    b = GenomicFeature("chr1", 4800, 6000, "+")
    c = GenomicFeature("chr2", 1000, 5000, "+")

    print(a.describe())  # GenomicFeature chr1:1000-5000(+)
    print(a.length())  # 4001
    print(a.overlaps(b))  # True  (4800-5000 shared)
    print(a.overlaps(c))  # False (different chromosome)
    #GenomicFeature("chr1", 5000, 1000, "+")  # should raise ValueError

    features = [
        GenomicFeature("chr1", 1000, 5000, "+"),
        Exon("chr1", 1000, 1200, "+", 1),
        Exon("chr1", 3000, 3300, "+", 2),
    ]
    for feature in features:
        print(feature.describe())







