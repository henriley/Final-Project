import unittest
import sqlite3

DBNAME='Pokemon.db'

class TestStats(unittest.TestCase):

    def test_1(self):
        conn = sqlite3.connect(DBNAME)
        cur = conn.cursor()

        sql = 'SELECT Name FROM PokemonStats'
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertIn(('bulbasaur',), result_list)
        self.assertIn(('charmander',), result_list)
        self.assertIn(('squirtle',), result_list)

        sql = '''
            SELECT HP, Attack, Defense, SpecialAttack, SpecialDefense, Speed
            FROM PokemonStats
            WHERE Name = 'squirtle'
        '''
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertEqual(len(result_list), 1)
        self.assertEqual(result_list[0][0], 44)

        sql = '''
            SELECT PokeDexNumber
            FROM PokemonStats
            WHERE Name = 'treecko'
        '''
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertEqual(len(result_list), 1)
        self.assertEqual(result_list[0][0], 252)

        sql = '''
            SELECT Ability1, Ability2, HiddenAbility
            FROM PokemonStats
            WHERE Name = 'pidgey'
        '''
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertEqual(len(result_list[0]), 3)
        self.assertEqual(result_list[0][1], 'tangled-feet')

        conn.close()

class TestAbility(unittest.TestCase):

    def test_2(self):
        conn = sqlite3.connect(DBNAME)
        cur = conn.cursor()

        sql = '''
            SELECT AbilityInfo
            FROM Abilities
            WHERE AbilityName = 'overgrow'
        '''
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertIn(('When this Pokémon has 1/3 or less of its HP remaining, its grass-type moves inflict 1.5× as much regular damage.',), result_list)
        self.assertEqual(len(result_list), 1)

        sql = '''
            SELECT AbilityId
            FROM Abilities
            WHERE AbilityName = 'bulletproof'
        '''
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertEqual(result_list[0][0], 171)

        conn.close()

class TestEvolutions(unittest.TestCase):

    def test_3(self):
            conn = sqlite3.connect(DBNAME)
            cur = conn.cursor()

            sql = '''
                SELECT Stage1, Stage2, Stage3
                FROM Evolutions
                WHERE Stage1 = 'chikorita'
            '''
            results = cur.execute(sql)
            result_list = results.fetchall()
            self.assertEqual(len(result_list[0]), 3)
            self.assertEqual(result_list[0][0], 'chikorita')
            self.assertEqual(result_list[0][1], 'bayleef')
            self.assertEqual(result_list[0][2], 'meganium')
            conn.close()

class TestDeviantArt(unittest.TestCase):

    def test_4(self):
            conn = sqlite3.connect(DBNAME)
            cur = conn.cursor()

            sql = '''
                SELECT DeviantURL
                FROM DeviantArt
                WHERE Name = 'turtwig'
            '''
            results = cur.execute(sql)
            result_list = results.fetchall()
            self.assertEqual(len(result_list), 1)
            conn.close()

unittest.main()
