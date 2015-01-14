import pytest

def test_bird_species():
    import B_sets as B
    assert len(B.bird_species) == 3, "bird_species should contain 3 things"

def test_difference():
    import B_sets as B
    my_bird_sightings = {"Lesser spotted notreallytherehawk",
                         "Invisible pink pigeon",
                        }
    my_bird_sightings.add(list(B.bird_species)[0])
    assert B.different_bird_species(my_bird_sightings) == \
        {"Lesser spotted notreallytherehawk",
         "Invisible pink pigeon",
        }
