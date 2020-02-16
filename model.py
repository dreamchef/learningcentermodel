#!/usr/bin/env python3

import random

class LearningCenter:
    def __init__(self, learners):
        self.learners = learners

class Learner:
    def __init__(self, relationships, personality, intelligence, interests):
        self.relationships = relationships
        self.experiences   = None
        self.personality   = personality
        self.intelligence  = intelligence
        self.interests     = interests
    def __str__(self):
        return ("-----personality-----\n" + str(self.personality) +
        "\n-----intelligence-----\n" + str(self.intelligence))
    def interact():
        return 0
        #TODO: interaction mechanic
    def participate():
        return 0
        #TODO: participation in activity mechanic

class Relationship:
    def __init__(self, memberindices, trust, empathy, primaryDyanamic, secondaryDynamic):
        self.memberindices    = memberindices
        self.trust            = trust
        self.empathy          = empathy
        self.primaryDyanamic  = primaryDyanamic # adversarial, neutral, cooperative
        self.secondaryDynamic = secondaryDynamic #competitive, balanced, nurturing

class Experience:
    def __init__(self, learners):
        self.learners = learners
        #TODO: more properties

# Based on Big Five
class Personality:
    def __init__(self, openness, conscientiousness, extraversion, agreeableness, neuroticism):
        self.openness = openness
        self.conscientiousness = conscientiousness
        self.extraversion = extraversion
        self.agreeableness = agreeableness
        self.neuroticism = neuroticism
    def __str__(self):
        return ("openness " + str(self.openness) + "\nconscientiousness " +
        str(self.conscientiousness) + "\nextraversion " + str(self.extraversion) +
        "\nagreeableness " + str(self.agreeableness) + "\nneuroticism " + str(self.neuroticism))

# Based on cognitive-contextual theory by Howard Gardner
class Intelligence:
    def __init__(self, visualSpatial, lingVerbal, interpersonal, intrapersonal,
                logicMath, musical, bodilyKin, naturalistic):
        self.visualSpatial = visualSpatial
        self.lingVerbal    = lingVerbal
        self.interpersonal = interpersonal
        self.intrapersonal = intrapersonal
        self.logicMath     = logicMath
        self.musical       = musical
        self.bodilyKin     = bodilyKin
        self.naturalistic  = naturalistic
    def __str__(self):
        return ("visualSpatial " + str(self.visualSpatial) + "\nlingVerbal " + str(self.lingVerbal) +
        "\ninterpersonal " + str(self.interpersonal) + "\nintrapersonal " + str(self.intrapersonal) +
        "\nlogicMath " + str(self.logicMath) + "\nmusical " + str(self.musical) + "\nbodilyKin " +
        str(self.bodilyKin) + "\nnaturalistic " + str(self.naturalistic))

# Loosely based on "The Construct of Interest" theory by Andreas Krapp
class Interest:
    def __init__(self, persistence, orientation):
        self.persistence  = persistence
        self.orientation  = orientation
    def __str__(self):
        return ("persistence " + str(self.persistence) + "\norientation " +
        str(self.orientation))

# ------------------------------------------------------------------------------

POPSIZE  = 10000
STDRANGE = 9

learners = []

# Randomly generate learner population
for lx in range(POPSIZE):

    print(lx)
    # Initial personality configuration
    openness          = random.randint(0, STDRANGE)
    conscientiousness = random.randint(0, STDRANGE)
    extraversion      = random.randint(0, STDRANGE)
    agreeableness     = random.randint(0, STDRANGE)
    neuroticism       = random.randint(0, STDRANGE)
    personality       = Personality(openness, conscientiousness, extraversion,
                        agreeableness, neuroticism)

    # Initial intelligence configuration
    visualSpatial = random.randint(0, STDRANGE)
    lingVerbal    = random.randint(0, STDRANGE)
    interpersonal = random.randint(0, STDRANGE)
    intrapersonal = random.randint(0, STDRANGE)
    logicMath     = random.randint(0, STDRANGE)
    musical       = random.randint(0, STDRANGE)
    bodilyKin     = random.randint(0, STDRANGE)
    naturalistic  = random.randint(0, STDRANGE)
    intelligence  = Intelligence(visualSpatial, lingVerbal, interpersonal,
                    intrapersonal, logicMath, musical, bodilyKin, naturalistic)

    # Initial interests configuration - assume learner has one interest
    persistence  = random.randint(0, STDRANGE)
    orientation  = random.choice(['modeling', 'emotional', 'intellectual', 'social'])
    interest     = Interest(persistence, orientation)

    # Initial relationship configuration - assume each learner has, on average,
    # relationships with two other learners
    if lx == 0:
        learners.append(Learner([], personality, intelligence, [interest]))
    else:
        priorRelationship = Relationship([lx, random.randint(0,lx-1)],
                            random.randint(0, STDRANGE), random.randint(0, STDRANGE),
                            random.choice(['adversarial', 'neutral', 'cooperative']),
                            random.choice(['competitive', 'balanced', 'nurturing']))
        learners.append(Learner([priorRelationship], personality, intelligence,
                                                                    [interest]))

print(str(POPSIZE) + ' learners instantiated!')

theNewSchool = LearningCenter(learners)

print('Learning center instantiated!')

while(1):
    learnerRequested = input("Enter learner index to view personality and intelligence profiles: ")
    print(learners[int(learnerRequested)])

# ------------------------------------------------------------------------------

# Run learners through randomized experiences and random grouping methods

EXPEREINCECOUNT = 100

for ex in range(EXPERIENCECOUNT):

    currentExperience = Experience()






    # -
