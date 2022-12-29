import random

def create_population(size):
    a=[]
    for i in range(n):
        a.append(random.randint(1, n))
    return a


def fitness(population, n):
    fitnes_array =[]
    for chromosomes in population:
        # print("chromosomes")
        # print(chromosomes)
        horizontal_collisions = sum([chromosomes.count(queen) - 1 for queen in chromosomes]) / 2
        diagonal_collisions = 0
        for i, col in enumerate(chromosomes):
            for j, diagonal in enumerate(chromosomes):
                mod = abs(i - j)
                if i != j:
                    if diagonal + mod == col or diagonal - mod == col:
                        diagonal_collisions += 1
        diagonal_collisions /= 2
        # print("fitness")
        fitnes_array.append(int(max_fitness - (horizontal_collisions + diagonal_collisions)))
        # print(fitnes_array)
    return fitnes_array

def crossover(chrom1, chrom2):
    length = len(chrom1)
    point = random.randint(0, length-1)
    # print(point)
    # print(chrom1[0:point] + chrom2[point:length])
    return chrom1[0:point] + chrom2[point:length]

def mutate(child):
    length = len(child)
    index = random.randint(0, length -1 )
    # print(index)
    rand_num = random.randint(1, length)
    # print(rand_num)
    child[index] = rand_num
    # print(child)
    return child

def select(population, fitness):
    selected = []
    selected = population.copy()
    # print("selected")
    min_index = fitness.index(min(fitness))
    selected.pop(min_index)

    # print(selected)
    return selected


def GA(population, n, mutation_threshold, fitness):
    new_population = []
    selected_population = select(population, fitness_array)
    # print("selected_population")
    # print(selected_population)
    for i in range(len(population)):
        a = random.sample(range(0, len(selected_population)), 2)
        # print(a)
        x = selected_population[a[0]]
        y = selected_population[a[1]]

        # x = selected_population[random.randint(0, len(selected_population)-1)]
        # print("x")
        # print(x)
        # y = selected_population[random.randint(0, len(selected_population)-1)]
        while x == y :
            # print("im working")
            x = selected_population[random.randint(0, len(selected_population)-1)]
            y = selected_population[random.randint(0, len(selected_population)-1)]
            # print(y)
        # print("y")
        # print(y)
        child = crossover(x,y)
        # print("child")
        # print(child)
        if random.random() < mutation_threshold:
            child = mutate(child)
            # print("child after mutate")
            # print(child)
        new_population.append(child)

    return new_population



n = 8
start_population =10
mutation_threshold = 0.6
max_fitness = (n * (n-1))/2
# print("max fitness")
# print(max_fitness)
population =[]
for i in range (start_population):
    population.append(create_population(n))

# print(population)
# print(type(population))
fitness_array = fitness(population,n)
#print(fitness_array)
total_fitness = sum(fitness_array)
# print("total fitness")
# print(total_fitness)

iteration = 1

while not max_fitness in fitness_array:
    # print(type(population))
    population = GA(population, n, mutation_threshold, fitness)
    # print("while loop population")
    # print(population)
    fitness_array = fitness(population, n)
    # print("while loop fitness")
    # print(fitness_array)
    iteration += 1

print("iteration needed")
print(iteration)
print(fitness_array)