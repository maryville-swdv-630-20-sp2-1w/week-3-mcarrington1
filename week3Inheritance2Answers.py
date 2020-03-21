class Spell:
      def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

      def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.get_description()

      def get_description(self):
        return 'No description'

      def execute(self):
        print(self.incantation)

class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')
        
    def get_description(self):
        return 'This charm summons an object to the caster, potentially over a significant distance.'

class Confundo(Spell):
      def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

      def get_description(self):
        return 'Causes the victim to become confused and befuddled.'

def study_spell(spell):
    print(spell)

spell = Accio()
spell.execute()
study_spell(spell)
study_spell(Confundo())

'''
1. Parent = Spell, Child = Accio, Confundo
2. Base = Spell, Sub = Accio, Confundo
3. Output below:
Accio
Summoning Charm Accio
No description
Confundus Charm Confundo
Causes the victim to become confused and befuddled.
4. get_description(self) from Confundo class is executed because we are overriding the Spell base class get_description method
5. see line 19-20. We are adding a get_description method that will override Spell base class
'''