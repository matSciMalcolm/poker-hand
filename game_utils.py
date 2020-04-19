#Game Utils


class GameState:
    '''
    Tracks the games progress and members
    '''
    
    small_blind_msg = 'Enter a value for the small blind '
    big_blind_msg = 'Enter a value for the big blind '
    num_players_msg = 'Enter the number of players including yourself '
    player_position_msg = 'How many seats away is the dealer? '
    
    def __init__(self):
        self.players = {}
        self.phase = 'start'
        self.small_blind = 10
        self.big_blind = 20
        self.pot_value = 0
        self.num_players = 10
        
    def setup(self):
        '''
        Set up a game of poker. 
        '''
        
        self.small_blind = float(input(self.small_blind_msg) or '10.00')
        self.big_blind = float(input(self.big_blind_msg) or '20.00')
        self.num_players = int(input(self.num_players_msg) or '10')
        
        for n in range(1, self.num_players):
            name = f'player_{n}'
            self.players[name] = Player(player_id = name)
            
        self.players[f'player_{int(input(self.player_position_msg) or "1")}'].user_flag = True
    
    def get_players(self):
        return self.players.values()
    
    def get_user(self):
        for player in self.get_players():
            if player.user_flag:
                return player

            
class Player:
    '''
    Represents a player in the game
    '''
    
    def __init__(self, player_id):
        self.player_id = player_id
        self.hand = Hand()
        self.user_flag = False

        
class Hand:
    '''
    Represents a players hand of cards
    '''
    
    def __init__(self):
        self.cards = []
        self.num_cards = len(self.cards)
        
    def add_card(self, card):
        self.cards.append(card)

        
class Card:
    '''
    A playing card
    '''
    suits = {'h': 'Hearts',
             'H': 'Hearts',
             'c': 'Clubs',
             'C': 'Clubs',
             's': 'Spades',
             'S': 'Spades',
             'd': 'Diamonds',
             'D': 'Diamonds'}
    
    ranks = {'a': 'Ace',
             'A': 'Ace',
             'q': 'Queen',
             'Q': 'Queen',
             'k': 'King',
             'K': 'King',
             'j': 'Jack',
             'J': 'Jack'}
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.rank_name = self.ranks[self.rank]
        self.suit = suit
        self.suit_name = self.suits[self.suit]
        self.value = f'{rank}{suit}'
        
    def __repr__(self):
        return f'{self.rank_name} of {self.suit_name}'
        
    def __str__(self):
        return f'{self.rank_name} of {self.suit_name}'


class GameLoop:
    '''
    Runs the game - all game logic.
    '''
    quit_game_message = 'Would you like to quit (y/n)? '
    
    def __init__(self):
        self.max_time = 60
        self.end_game = False
        
    def run(self):
        '''
        Main loop for game
        '''
        
        self.end_game = self._check_quit(input(self.quit_game_message))    
            
        while not self.end_game:
            if game_time < max_time:
                while self.game_state.phase != 'end':
                    #run phase
                    run_phase()
                    #update state
                    update_state
                    
    def _check_quit(self, quit):
        '''
        Check if player has ended game
        '''
        if any(quit == i for i in ['y', 'Y']):
            return True
        else:
            return False
                    
    def run_phase(self):
        '''
        Executes a game phase
        '''
        # collect game information on
        # collect bets
    
    def _parse_card(self, card):
        return card[0], card[1]
        
    def deal(self):
        '''
        Request information about cards dealt to a player
        '''
        user = self.game_state.get_user()
        for card in range(1,3):
            card_request_message = f'Please enter the {card} card you were dealt as "RankSuit" i.e "AH" '
            user.hand.add_card(Card(*self._parse_card(input(card_request_message))))
                
    def setup(self, game_state):
        self.game_state = game_state
        self.game_state.setup()
        self.deal()
        self.game_time = 0