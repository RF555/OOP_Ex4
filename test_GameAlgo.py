from unittest import TestCase

from GameAlgo import *

#  GRAPH srt:
A0_str = 'data\A0'
A1_str = 'data\A1'
A2_str = 'data\A2'
A3_str = 'data\A3'

# POKEMON str
poke_0_str = '{"Pokemons": [{"Pokemon": {"value": 5.0,"type": -1,"pos": "35.197656770719604,32.10191878639921,0.0"}}]}'
poke_3_str = '{"Pokemons":[{"Pokemon":{"value":5.0,"type":-1,"pos":"35.197656770719604,32.10191878639921,0.0"}},' \
             '{"Pokemon":{"value":8.0,"type":-1,"pos":"35.199963710098416,32.105723673136964,0.0"}},{"Pokemon":{' \
             '"value":13.0,"type":-1,"pos":"35.195224052340706,32.10575624080796,0.0"}},{"Pokemon":{"value":5.0,' \
             '"type":-1,"pos":"35.19494883961552,32.105809680537625,0.0"}}]} '
poke_5_str = '{"Pokemons":[{"Pokemon":{"value":5.0,"type":-1,"pos":"35.188900353135324,32.105320110855615,0.0"}},' \
             '{"Pokemon":{"value":8.0,"type":-1,"pos":"35.206679711961414,32.10571613186106,0.0"}},{"Pokemon":{' \
             '"value":13.0,"type":-1,"pos":"35.212669424769075,32.105340746955505,0.0"}},{"Pokemon":{"value":5.0,' \
             '"type":-1,"pos":"35.21120742821597,32.10240519983585,0.0"}},{"Pokemon":{"value":9.0,"type":-1,' \
             '"pos":"35.2107064115802,32.10181728154006,0.0"}},{"Pokemon":{"value":12.0,"type":-1,' \
             '"pos":"35.20704629752213,32.105471692111855,0.0"}}]} '
poke_7_str = '{"Pokemons":[{"Pokemon":{"value":5.0,"type":-1,"pos":"35.188900353135324,32.105320110855615,0.0"}},' \
             '{"Pokemon":{"value":8.0,"type":-1,"pos":"35.206679711961414,32.10571613186106,0.0"}}]} '
poke_9_str = '{"Pokemons":[{"Pokemon":{"value":5.0,"type":-1,"pos":"35.20273974670703,32.10439601193746,0.0"}},' \
             '{"Pokemon":{"value":8.0,"type":-1,"pos":"35.189541903742466,32.10714473742062,0.0"}},{"Pokemon":{' \
             '"value":5.0,"type":-1,"pos":"35.20418622066997,32.10618391544376,0.0"}},{"Pokemon":{"value":9.0,' \
             '"type":-1,"pos":"35.207511563168026,32.10516145234799,0.0"}}]} '
poke_15_str = '{"Pokemons":[{"Pokemon":{"value":5.0,"type":-1,"pos":"35.20392770907119,32.10833067124629,0.0"}},' \
              '{"Pokemon":{"value":8.0,"type":-1,"pos":"35.20622459040522,32.101281022067994,0.0"}},{"Pokemon":{' \
              '"value":5.0,"type":-1,"pos":"35.21200574506042,32.105721621191464,0.0"}},{"Pokemon":{"value":9.0,' \
              '"type":1,"pos":"35.212532074496366,32.106982780342726,0.0"}}]} '

# AGENTS
a1_str = '{"Agents":[{"Agent":{"id":0,"value":0.0,"src":0,"dest":1,"speed":1.0,"pos":"35.18753053591606,' \
         '32.10378225882353,0.0"}}]} '
a3_str = '{"Agents":[' \
         '{"Agent":{"id":0,"value":0.0,"src":0,"dest":1,"speed":1.0,"pos":"0,0,0.0"}},' \
         '{"Agent":{"id":1,"value":0.0,"src":1,"dest":2,"speed":2.0,"pos":"1,1,0.0"}},' \
         '{"Agent":{"id":2,"value":0.0,"src":2,"dest":3,"speed":3.0,"pos":"2,2,0.0"}}' \
         ']} '

a5_str = '{"Agents":[' \
         '{"Agent":{"id":0,"value":0.0,"src":0,"dest":1,"speed":1.0,"pos":"0,0,0.0"}},' \
         '{"Agent":{"id":1,"value":0.0,"src":1,"dest":2,"speed":2.0,"pos":"1,1,0.0"}},' \
         '{"Agent":{"id":2,"value":0.0,"src":2,"dest":3,"speed":3.0,"pos":"2,2,0.0"}},' \
         '{"Agent":{"id":3,"value":0.0,"src":3,"dest":4,"speed":4.0,"pos":"3,3,0.0"}},' \
         '{"Agent":{"id":4,"value":0.0,"src":4,"dest":5,"speed":5.0,"pos":"4,4,0.0"}},' \
         '{"Agent":{"id":5,"value":0.0,"src":5,"dest":6,"speed":6.0,"pos":"5,5,0.0"}}' \
         ']} '
a7_str = '{"Agents":[' \
         '{"Agent":{"id":0,"value":0.0,"src":0,"dest":1,"speed":1.0,"pos":"0,0,0.0"}},' \
         '{"Agent":{"id":1,"value":0.0,"src":1,"dest":2,"speed":2.0,"pos":"1,1,0.0"}},' \
         '{"Agent":{"id":2,"value":0.0,"src":2,"dest":3,"speed":3.0,"pos":"2,2,0.0"}},' \
         '{"Agent":{"id":3,"value":0.0,"src":3,"dest":4,"speed":4.0,"pos":"3,3,0.0"}},' \
         '{"Agent":{"id":4,"value":0.0,"src":4,"dest":5,"speed":5.0,"pos":"4,4,0.0"}},' \
         '{"Agent":{"id":5,"value":0.0,"src":5,"dest":6,"speed":6.0,"pos":"5,5,0.0"}},' \
         '{"Agent":{"id":6,"value":0.0,"src":6,"dest":7,"speed":7.0,"pos":"6,6,0.0"}},' \
         '{"Agent":{"id":7,"value":0.0,"src":7,"dest":8,"speed":8.0,"pos":"7,7,0.0"}}' \
         ']} '


class TestGameAlgo(TestCase):

    def test_init_pokemons(self):
        game: GameAlgo = GameAlgo()
        self.assertTrue(game.pokemons.is_empty())
        game.init_pokemons(poke_0_str)
        self.assertEqual(game.pokemons.size(), 1)
        self.assertEqual(game.pokemons.peek()[2].value, 5)
        game.init_pokemons(poke_3_str)
        self.assertEqual(game.pokemons.size(), 4)
        self.assertEqual(game.pokemons.peek()[2].value, 13)
        game.init_pokemons(poke_5_str)
        self.assertEqual(game.pokemons.size(), 6)
        self.assertEqual(game.pokemons.peek()[2].value, 13)
        game.init_pokemons(poke_7_str)
        self.assertEqual(game.pokemons.size(), 2)
        self.assertEqual(game.pokemons.peek()[2].value, 8)
        game.init_pokemons(poke_9_str)
        self.assertEqual(game.pokemons.size(), 4)
        self.assertEqual(game.pokemons.peek()[2].value, 9)
        game.init_pokemons(poke_15_str)
        self.assertEqual(game.pokemons.size(), 4)
        self.assertEqual(game.pokemons.peek()[2].value, 9)

    def test_init_agents(self):
        game: GameAlgo = GameAlgo()
        game.init_agents(a3_str)
        self.assertEqual(len(game.agents), 3)
        for id, agent_ in game.agents.items():
            self.assertEqual(agent_.id, id)
            self.assertEqual(agent_.src, id)
            self.assertEqual(agent_.dst, id + 1)
            self.assertEqual(agent_.speed, id + 1)
            self.assertEqual(agent_.pos, str(id) + "," + str(id) + ',' + str(0.0))
        game.init_agents(a5_str)
        self.assertEqual(len(game.agents), 6)
        for id, agent_ in game.agents.items():
            self.assertEqual(agent_.id, id)
            self.assertEqual(agent_.src, id)
            self.assertEqual(agent_.dst, id + 1)
            self.assertEqual(agent_.speed, id + 1)
            self.assertEqual(agent_.pos, str(id) + "," + str(id) + ',' + str(0.0))
        game.init_agents(a7_str)
        self.assertEqual(len(game.agents), 8)
        for id, agent_ in game.agents.items():
            self.assertEqual(agent_.id, id)
            self.assertEqual(agent_.src, id)
            self.assertEqual(agent_.dst, id + 1)
            self.assertEqual(agent_.speed, id + 1)
            self.assertEqual(agent_.pos, str(id) + "," + str(id) + ',' + str(0.0))

    # def test_allocate_all_agents(self):
    #     self.fail()
    #
    # def test_choose_agent(self):
    #     self.fail()
    #
    # def test_time_to_poke(self):
    #     self.fail()
    #
    # def test_find_pok_src_dst(self):
    #     self.fail()
    #
    # def test_find_dist_nodes(self):
    #     self.fail()
    #
    # def test_all_pok_src_dst(self):
    #     self.fail()

