class Settings:
    def __init__(self):
        ## screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (255, 180, 80)

        # ending the game if it crosses the
        self.kodanda_limit = 3

        ## Ramastra :-
        """ adding ramastra(image version) settinga """
        #static ramastra speed
        # self.ramastra_speed = 3.8
        self.ramastras_allowed = 10

        """ if u wanna add ramastra as solid colour rects """
        # self.ramastra_width =
        # self.ramastra_height =
        # self.ramastra_color =

        ## Danav :-
        #static danav speed:-
        # self.danav_speed = .6
        self.sena_direction = +1.1
        # sena_direction of 1 represents right; -1 represents left.
        self.sena_down_speed = +5

        # factor with which the speeds increasing every leveling up
        self.upspeed = 1.1

        # scoring increasing factor
        self.upscore = 2.0

        # in case you want static speed uncomment the above settings
        # and comment the dynamic settings
    def init_dynamic_settings(self):
        self.kodanda_speed = 1.2
        self.danav_speed = 1.1
        self.ramastra_speed = 2.0

        #fleet direction
        self.sena_direction = 1

        # points for a danav
        self.danav_points = 10

    def speed_increament(self):
        """ speed settings and points for every danav ramastra collision """
        self.ramastra_speed *= self.upspeed
        self.danav_speed *= self.upspeed
        self.kodanda_speed *= self.upspeed

        self.danav_points = int(self.danav_points*self.upscore)