from otree.api import *
import time

c = Currency  # old name for currency; you can delete this.


class Constants(BaseConstants):
    name_in_url = "ch1_1_risk"
    players_per_group = None
    num_rounds = 1
    Q_num = 5
    categories = (["Aが1つ", "Aが2つ", "Aが3つ", "Aが4つ", "Aが5つ"],)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name = models.StringField(
        initial = 'Unknown',
        blank = False,
        varbose_name = 'あなたの名前を教えてください'
        )

    # 1：Decision_1
    risk_List = models.StringField(initial="")
    individual_choice_r_comment = models.StringField(initial="", label="")
    List_A = models.LongStringField(initial="")
    List_B = models.LongStringField(initial="")
    num_A = models.IntegerField()
    multiple_switch = models.BooleanField()

    start = models.FloatField(initial=0.0)
    read_time = models.LongStringField(initial="0")
    time = models.LongStringField(initial="0")

    # Decision_2
    individual_choice = models.StringField(initial="", label="")
    individual_choice_comment = models.StringField(initial="", label="")

    # Decision_3
    u_individual_choice = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        verbose_name="",
        choices=[
            ["A", "Aをえらぶ"],
            ["B", "Bをえらぶ"],
        ],
    )

    individual_choice_u_comment = models.StringField(initial="", label="")

    # Decision_4
    s_individual_choice = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        verbose_name="",
        choices=[
            ["A", "Aをえらぶ"],
            ["B", "Bをえらぶ"],
        ],
    )

    individual_choice_s_comment = models.StringField(initial="", label="")

    # Decision_5
    e_individual_choice = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        verbose_name="",
        choices=[
            ["A", "Aをえらぶ"],
            ["B", "Bをえらぶ"],
        ],
    )
    individual_choice_e_comment = models.StringField(initial="", label="")


# PAGES-----
class Decision(Page):
    form_model = "player"
    form_fields = ["name","individual_choice_r_comment"]
    #  html to サーバー
    @staticmethod
    def live_method(player: Player, data):
        if data["first"] == 1:
            player.time = str(time.time() - player.start)
            player.risk_List = "A" * len(data["A"]) + "B" * len(data["B"])
            player.multiple_switch = 0
            player.num_A = player.risk_List.count("A")
        else:
            player.time = str(time.time() - player.start)
            risklist = player.risk_List
            if data["select_type"] == "A":
                player.risk_List = (
                    risklist[: int(data["position_num"]) - 1]
                    + "A"
                    + risklist[int(data["position_num"]) :]
                )
            else:
                player.risk_List = (
                    risklist[: int(data["position_num"]) - 1]
                    + "B"
                    + risklist[int(data["position_num"]) :]
                )
            player.num_A = player.risk_List.count("A")
            player.multiple_switch = "B" in player.risk_List[: player.num_A]

    # @staticmethod
    # def before_next_page(self, timeout_happened):
    #    self.participant.vars['MPL_result'] = self.MPL_List


class Decision_2(Page):
    form_model = "player"
    form_fields = ["individual_choice", "individual_choice_comment"]


class Decision_3(Page):
    form_model = "player"
    form_fields = ["u_individual_choice", "individual_choice_u_comment"]


class Decision_4(Page):
    form_model = "player"
    form_fields = ["s_individual_choice", "individual_choice_s_comment"]


class Decision_5(Page):
    form_model = "player"
    form_fields = ["e_individual_choice", "individual_choice_e_comment"]

class ResultsWaitPage(WaitPage):
    pass


class PreResults(Page):
    pass


page_sequence = [
    Decision,
    # Decision_2,
    Decision_3,
    Decision_4,
    Decision_5,
    ResultsWaitPage,
    PreResults
]
