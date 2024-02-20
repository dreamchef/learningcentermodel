#!/usr/bin/env python3

import random

class LearningGroup:
    def __init__(self):
        self.learners = []

class Learner:
    def __init__(self, ID):
        self.ID            = ID
        self.alignment     = []
        self.experiences   = []
        self.relationships = []
        self.personality   = Personality()
        self.intelligence  = Intelligence()

    def __str__(self):
        # relationshipsIndices = []
        # for rx in range(len(self.relationships)):
        #     for mx in range(len(self.relationships[rx].memberindices)):
        #         print(str(self.relationships[rx].memberindices[mx]) + str(self.ID))
        #         if self.relationships[rx].memberindices[mx] != self.ID:
        #             relationshipsIndices.append(self.relationships[rx].memberindices[mx])
        # return ("-----personality-----\n" + str(self.personality) +
        # "\n-----intelligence-----\n" + str(self.intelligence) +
        # "\n-----relationships-----\n" + str(relationshipsIndices))

        return ("-----personality-----\n" + str(self.personality) +
        "\n-----intelligence-----\n" + str(self.intelligence))

# Based on Big Five
class Personality:
    def __init__(self):
        self.openness          = random.randint(0, STDRANGE)
        self.conscientiousness = random.randint(0, STDRANGE)
        self.extraversion      = random.randint(0, STDRANGE)
        self.agreeableness     = random.randint(0, STDRANGE)
        self.neuroticism       = random.randint(0, STDRANGE)
    def __str__(self):
        return ("openness " + str(self.openness) + "\nconscientiousness " +
        str(self.conscientiousness) + "\nextraversion " + str(self.extraversion) +
        "\nagreeableness " + str(self.agreeableness) + "\nneuroticism " + str(self.neuroticism))

# Based on cognitive-contextual theory by Howard Gardner
class Intelligence:
    def __init__(self):
        self.visualSpatial = random.randint(0, STDRANGE)
        self.lingVerbal    = random.randint(0, STDRANGE)
        self.interpersonal = random.randint(0, STDRANGE)
        self.intrapersonal = random.randint(0, STDRANGE)
        self.logicMath     = random.randint(0, STDRANGE)
        self.musical       = random.randint(0, STDRANGE)
        self.bodilyKin     = random.randint(0, STDRANGE)
        self.naturalistic  = random.randint(0, STDRANGE)
    def __str__(self):
        return ("visualSpatial " + str(self.visualSpatial) + "\nlingVerbal " + str(self.lingVerbal) +
        "\ninterpersonal " + str(self.interpersonal) + "\nintrapersonal " + str(self.intrapersonal) +
        "\nlogicMath " + str(self.logicMath) + "\nmusical " + str(self.musical) + "\nbodilyKin " +
        str(self.bodilyKin) + "\nnaturalistic " + str(self.naturalistic))

class Experience:
    def __init__(self, learners):
        self.learners = learners
        #TODO: more properties

# Loosely based on "The Construct of Interest" theory by Andreas Krapp
class Interest:
    def __init__(self, persistence, orientation):
        self.persistence  = persistence
        self.orientation  = orientation
    def __str__(self):
        return ("persistence " + str(self.persistence) + "\norientation " +
        str(self.orientation))

#TOFIX: Relationships are one-sided.  Only exist in the relationships list of one member.
class Relationship:
    def __init__(self, memberindices, trust, empathy, primaryDyanamic, secondaryDynamic):
        self.memberindices    = memberindices
        self.trust            = trust
        self.empathy          = empathy
        self.primaryDyanamic  = primaryDyanamic # adversarial, neutral, cooperative
        self.secondaryDynamic = secondaryDynamic #competitive, balanced, nurturing

# ------------------------------------------------------------------------------

POPSIZE  = 400
STDRANGE = 9

theNewSchool = LearningCenter()
print('Learning center instantiated!')

# Randomly generate learner population
for lx in range(POPSIZE):

    # Initial interests configuration - assume learner has one interest
    persistence  = random.randint(0, STDRANGE)
    orientation  = random.choice(['modeling', 'emotional', 'intellectual', 'social'])
    initialInterest     = Interest(persistence, orientation)

    # Initial relationship configuration - assume each learner has, on average,
    # relationships with two other learners
    if lx == 0:
        theNewSchool.learners.append(Learner(lx))
        theNewSchool.learners[lx].interests.append(initialInterest)
    else:
        theNewSchool.learners.append(Learner(lx))
        initialRelationship = Relationship([lx, random.randint(0,lx-1)],
                            random.randint(0, STDRANGE), random.randint(0, STDRANGE),
                            random.choice(['adversarial', 'neutral', 'cooperative']),
                            random.choice(['competitive', 'balanced', 'nurturing']))
        theNewSchool.learners[lx].relationships.append(initialRelationship)

print(str(POPSIZE) + ' learners instantiated!')

while(1):
    learnerRequested = input("Enter learner index to view personality and intelligence profiles: ")
    print(theNewSchool.learners[int(learnerRequested)])

# ------------------------------------------------------------------------------

# Run learners through randomized experiences and random grouping methods

EXPEREINCECOUNT = 100

for ex in range(EXPERIENCECOUNT):

    currentExperience = Experience()






    # -
