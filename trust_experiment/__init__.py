from otree.api import *
import random

doc = """
信頼ゲームの実験
"""


class C(BaseConstants):
    NAME_IN_URL = 'trust_experiment'
    PLAYERS_PER_GROUP = 2 #2人プレイヤー
    NUM_ROUNDS = 5 #5期のみ
    ENDOWMENT_1 = cu(10) #プレイヤー1の初期保有額は10ポイント
    ENDOWMENT_2 = cu(10) #プレイヤー1の初期保有額は10ポイント
    ENDOWMENT_3 = cu(10) #プレイヤー1の初期保有額は10ポイント
    ENDOWMENT_4 = cu(10) #プレイヤー1の初期保有額は10ポイント
    ENDOWMENT_5 = cu(10) #プレイヤー1の初期保有額は10ポイント
    MULTIPLIER = 3 #プレイヤー3はポイントを3倍にする

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    give_amount_1 = models.CurrencyField(
        choices = currency_range(cu(0), C.ENDOWMENT_1, cu(1)),
        #プレイヤー1がプレイヤー2に渡すポイント
        label = 'あなたはプレイヤー2にいくら渡しますか?',
        widget = widgets.RadioSelectHorizontal,
        #水平配置のラジオボタンで選択
    )
    give_amount_2 = models.CurrencyField(
        choices = currency_range(cu(0), C.ENDOWMENT_2, cu(1)),
        #プレイヤー1がプレイヤー2に渡すポイント
        label = 'あなたはプレイヤー2にいくら渡しますか?',
        widget = widgets.RadioSelectHorizontal,
        #水平配置のラジオボタンで選択
    )
    give_amount_3 = models.CurrencyField(
        choices = currency_range(cu(0), C.ENDOWMENT_3, cu(1)),
        #プレイヤー1がプレイヤー2に渡すポイント
        label = 'あなたはプレイヤー2にいくら渡しますか?(実際の選択です！)',
        widget = widgets.RadioSelectHorizontal,
        #水平配置のラジオボタンで選択
    )
    give_amount_4 = models.CurrencyField(
        choices = currency_range(cu(0), C.ENDOWMENT_4, cu(1)),
        #プレイヤー1がプレイヤー2に渡すポイント
        label = 'あなたはプレイヤー2にいくら渡しますか?',
        widget = widgets.RadioSelectHorizontal,
        #水平配置のラジオボタンで選択
    )
    give_amount_5 = models.CurrencyField(
        choices = currency_range(cu(0), C.ENDOWMENT_5, cu(1)),
        #プレイヤー1がプレイヤー2に渡すポイント
        label = 'あなたはプレイヤー2にいくら渡しますか?',
        widget = widgets.RadioSelectHorizontal,
        #水平配置のラジオボタンで選択
    )

    back_amount_1 = models.CurrencyField(
        label = 'あなたはプレイヤー1にいくら返しますか?',
        widget = widgets.RadioSelectHorizontal,
        #水平配置のラジオボタンで選択
    )
    back_amount_2 = models.CurrencyField(
        label = 'あなたはプレイヤー1にいくら返しますか?',
        widget = widgets.RadioSelectHorizontal,
        #水平配置のラジオボタンで選択
    )
    back_amount_3 = models.CurrencyField(
        label = 'あなたはプレイヤー1にいくら返しますか?(実際の選択です！)',
        widget = widgets.RadioSelectHorizontal,
        #水平配置のラジオボタンで選択
    )
    back_amount_4 = models.CurrencyField(
        label = 'あなたはプレイヤー1にいくら返しますか?',
        widget = widgets.RadioSelectHorizontal,
        #水平配置のラジオボタンで選択
    )
    back_amount_5 = models.CurrencyField(
        label = 'あなたはプレイヤー1にいくら返しますか?',
        widget = widgets.RadioSelectHorizontal,
        #水平配置のラジオボタンで選択
    )

    proposed_amount = models.CurrencyField(
        label ="あなたはプレイヤー2に何点渡すつもりか伝えてください（実際の選択とは別です）",
        choices = currency_range(cu(0), C.ENDOWMENT_3, cu(1)),
        widget = widgets.RadioSelectHorizontal,
    )
    promised_return = models.CurrencyField(
        label="プレイヤー1から提案された金額に対して，何点返すつもりか伝えてください（実際の選択とは別です）",
        widget = widgets.RadioSelectHorizontal,
    )

def back_amount_1_choices(group: Group):
    if group.give_amount_1 is None:
        return []
    return currency_range(cu(0),cu(group.give_amount_1 * C.MULTIPLIER),cu(1))
    #プレイヤー2が返すポイントの選択肢は0からプレイヤー1から受け取った
    #ポイントをC.MULTILIER倍したものまでとします

def back_amount_2_choices(group: Group):
    if group.give_amount_2 is None:
        return []
    return currency_range(cu(0),cu(group.give_amount_2 * C.MULTIPLIER),cu(1))
    #プレイヤー2が返すポイントの選択肢は0からプレイヤー1から受け取った
    #ポイントをC.MULTILIER倍したものまでとします

def back_amount_3_choices(group: Group):
    if group.give_amount_3 is None:
        return []
    return currency_range(cu(0),cu(group.give_amount_3 * C.MULTIPLIER),cu(1))
    #プレイヤー2が返すポイントの選択肢は0からプレイヤー1から受け取った
    #ポイントをC.MULTILIER倍したものまでとします

def back_amount_4_choices(group: Group):
    if group.give_amount_4 is None:
        return []
    return currency_range(cu(0),cu(group.give_amount_4 * C.MULTIPLIER),cu(1))
    #プレイヤー2が返すポイントの選択肢は0からプレイヤー1から受け取った
    #ポイントをC.MULTILIER倍したものまでとします

def back_amount_5_choices(group: Group):
    if group.give_amount_5 is None:
        return []
    return currency_range(cu(0),cu(group.give_amount_5 * C.MULTIPLIER),cu(1))
    #プレイヤー2が返すポイントの選択肢は0からプレイヤー1から受け取った
    #ポイントをC.MULTILIER倍したものまでとします

def promised_return_choices(group: Group):
    if group.proposed_amount is None:
        return []
    return currency_range(cu(0),cu(group.proposed_amount*C.MULTIPLIER),cu(1))

Page7timeout = models.IntegerField()
#Page7のタイムアウト時間を記録する変数
Page9timeout = models.IntegerField()
#Page9のタイムアウトを記録する変数
Page22timeout = models.IntegerField()
#Page22のタイムアウトを記録する変数


class Player(BasePlayer):
    name = models.StringField(
        initial = 'Unknown',
        blank = False,
        varbose_name = 'あなたの名前を教えてください'
        )

def compute_1(group: Group):
    p1 = group.get_player_by_id(1)
    #プレイヤー1の情報を取得
    p2 = group.get_player_by_id(2)
    #プレイヤー2の情報を取得
    give = group.field_maybe_none('give_amount_1') or cu(0)
    back = group.field_maybe_none('back_amount_1') or cu(0)

    p1.payoff = C.ENDOWMENT_1 - give + back
    p2.payoff = give * C.MULTIPLIER - back

def compute_2(group: Group):
    p1 = group.get_player_by_id(1)
    #プレイヤー1の情報を取得
    p2 = group.get_player_by_id(2)
    #プレイヤー2の情報を取得
    give = group.field_maybe_none('give_amount_2') or cu(0)
    back = group.field_maybe_none('back_amount_2') or cu(0)

    p1.payoff = C.ENDOWMENT_2 - give + back
    p2.payoff = give * C.MULTIPLIER - back


def compute_3(group: Group):
    p1 = group.get_player_by_id(1)
    #プレイヤー1の情報を取得
    p2 = group.get_player_by_id(2)
    #プレイヤー2の情報を取得
    give = group.field_maybe_none('give_amount_3') or cu(0)
    back = group.field_maybe_none('back_amount_3') or cu(0)

    p1.payoff = C.ENDOWMENT_3 - give + back
    p2.payoff = give * C.MULTIPLIER - back

def compute_4(group: Group):
    p1 = group.get_player_by_id(1)
    #プレイヤー1の情報を取得
    p2 = group.get_player_by_id(2)
    #プレイヤー2の情報を取得
    give = group.field_maybe_none('give_amount_4') or cu(0)
    back = group.field_maybe_none('back_amount_4') or cu(0)

    p1.payoff = C.ENDOWMENT_4 - give + back
    p2.payoff = give * C.MULTIPLIER - back

def compute_5(group: Group):
    p1 = group.get_player_by_id(1)
    #プレイヤー1の情報を取得
    p2 = group.get_player_by_id(2)
    #プレイヤー2の情報を取得
    give = group.field_maybe_none('give_amount_5') or cu(0)
    back = group.field_maybe_none('back_amount_5') or cu(0)

    p1.payoff = C.ENDOWMENT_5 - give + back
    p2.payoff = give * C.MULTIPLIER - back


def creating_session(self):
    players = self.get_players()
    num_players = len(players)

    # パーフェクト・ストレンジャー・マッチングが可能な人数かチェック
    if num_players % 2 != 0:
        raise ValueError("プレイヤー数は偶数である必要があります。")

    if self.round_number == 1:
        # ラウンド1ではランダムにグループ化
        self.group_randomly()
    else:
        # 前ラウンドまでのマッチ履歴を取得
        previous_pairs = set()
        for round_num in range(1, self.round_number):
            for group in self.in_round(round_num).get_groups():
                p1, p2 = group.get_players()
                previous_pairs.add(frozenset([p1.participant.code, p2.participant.code]))

        # 現ラウンドのペア候補をランダムシャッフルして作成
        attempts = 100
        for _ in range(attempts):
            shuffled = players[:]
            random.shuffle(shuffled)
            tentative_pairs = list(zip(shuffled[::2], shuffled[1::2]))

            # 一度も会ってない相手のみで構成できたらOK
            if all(frozenset([p1.participant.code, p2.participant.code]) not in previous_pairs
                    for p1, p2 in tentative_pairs):
                self.set_group_matrix([[p1, p2] for p1, p2 in tentative_pairs])
                return

        raise Exception("ペアが重複せずにマッチングできませんでした。プレイヤー数を見直してください。")

# PAGES
class Page1(Page):
    form_model = 'player'
    form_fields = ['name']

    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.round_number == 1

class Page2(WaitPage):
    pass
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.round_number == 1

class Page3(Page):
    form_model = 'group'
    form_fields = ['give_amount_1']
    #プレイヤー1がプレイヤー2に渡すポイントを入力する。

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1 and player.subsession.round_number == 1
        #プレイヤー1だけがこのページを表示する。

class Page4(WaitPage):
    pass
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.round_number == 1

class Page5(Page):
    form_model = 'group'
    form_fields = ['back_amount_1']
    #プレイヤー2がプレイヤー1に返すポイントを入力する。

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 2 and player.subsession.round_number == 1

        #プレイヤー2だけがこのページを表示する。

    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        give = group.field_maybe_none('give_amount_1') or cu(0)
        return dict(
            give_amount=give,
            multi_amount=give * C.MULTIPLIER
        )
        #group.give_amount_1 を　C.MULTIPLIER倍して，multi_amountとして
        #画面に表示できるようにする

class Page6(WaitPage):
    after_all_players_arrive = compute_1
    #全プレイヤーがこのページに到達したらcompute関数を実行する。
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.round_number == 1

class Page7(Page):
    pass
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.round_number == 1

class Page8(WaitPage):
    pass
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.round_number == 1

class Page9(Page):
    pass
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.round_number == 2

class Page10(Page):
    timeout_seconds = 10
    #Page4のタイムアウト時間を10秒に設定
    form_model = 'group'
    form_fields = ['give_amount_2']
    #プレイヤー1がプレイヤー2に渡すポイントを入力する。

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1 and player.subsession.round_number == 2
        #プレイヤー1だけがこのページを表示する。

class Page11(WaitPage):
    pass
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.round_number == 2

class Page12(Page):
    timeout_seconds = 10
    #Page9のタイムアウト時間を10秒に設定
    form_model = 'group'
    form_fields = ['back_amount_2']
    #プレイヤー2がプレイヤー1に返すポイントを入力する。

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 2 and player.subsession.round_number == 2
        #プレイヤー2だけがこのページを表示する。

    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        give = group.field_maybe_none('give_amount_2') or cu(0)
        return dict(
            give_amount = give,
            multi_amount = give * C.MULTIPLIER
        )
    #group.give_amount_2 を　C.MULTIPLIER倍して，multi_amountとして
    #画面に表示できるようにする

class Page13(WaitPage):
    after_all_players_arrive = compute_2
    #全プレイヤーがこのページに到達したらcompute関数を実行する。
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.round_number == 2

class Page14(Page):
    pass
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.round_number == 2

class Page15(WaitPage):
    pass
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.round_number == 2

class Page16(Page):
    form_model = 'group'
    form_fields = ['proposed_amount']

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1 and player.subsession.round_number == 3

class Page17(WaitPage):
    pass
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.round_number == 3

class Page18(Page):

    form_model = 'group'
    form_fields = ['promised_return']

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 2 and player.subsession.round_number == 3

    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        proposed = group.field_maybe_none('proposed_amount') or cu(0)
        return dict(
            proposed_amount =  proposed,
            proposed_multi = proposed * C.MULTIPLIER,
            max_return = list(currency_range(cu(0), cu(group.proposed_amount * C.MULTIPLIER), cu(1)))
        )


class Page19(WaitPage):
    pass
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.round_number == 3

class Page20(Page):
    form_model = 'group'
    form_fields = ['give_amount_3']
    #プレイヤー1がプレイヤー2に渡すポイントを入力する。

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1 and player.subsession.round_number == 3
        #プレイヤー1だけがこのページを表示する。

class Page21(WaitPage):
    pass
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.round_number == 3

class Page22(Page):
    form_model = 'group'
    form_fields = ['back_amount_3']
    #プレイヤー2がプレイヤー1に返すポイントを入力する。

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 2 and player.subsession.round_number == 3
        #プレイヤー2だけがこのページを表示する。

    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        give = group.field_maybe_none('give_amount_3') or cu(0)
        return dict(
            give_amount = give,
            multi_amount = give * C.MULTIPLIER
        )
    #group.give_amount_3 を　C.MULTIPLIER倍して，multi_amountとして
    #画面に表示できるようにする

class Page23(WaitPage):
    after_all_players_arrive = compute_3
    #全プレイヤーがこのページに到達したらcompute関数を実行する。
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.round_number == 3

class Page24(Page):
    pass
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.round_number == 3

class Page25(WaitPage):
    pass
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.round_number == 3

class Page26(Page):
    pass
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.round_number == 4

class Page27(WaitPage):
    pass
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.round_number == 4

class Page28(Page):
    timeout_seconds = 180
    #Page9のタイムアウト時間を180秒に設定
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.round_number == 4

class Page29(WaitPage):
    pass

class Page30(Page):
    form_model = 'group'
    form_fields = ['give_amount_4']
    #プレイヤー1がプレイヤー2に渡すポイントを入力する。

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1 and player.subsession.round_number == 4
        #プレイヤー1だけがこのページを表示する。

class Page31(WaitPage):
    pass
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.round_number == 4

class Page32(Page):
    form_model = 'group'
    form_fields = ['back_amount_4']
    #プレイヤー2がプレイヤー1に返すポイントを入力する。

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 2 and player.subsession.round_number == 4
        #プレイヤー2だけがこのページを表示する。

    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        give = group.field_maybe_none('give_amount_4') or cu(0)
        return dict(
            give_amount = give,
            multi_amount = give * C.MULTIPLIER
        )
    #group.give_amount_4 を　C.MULTIPLIER倍して，multi_amountとして
    #画面に表示できるようにする

class Page33(WaitPage):
    after_all_players_arrive = compute_4
    #全プレイヤーがこのページに到達したらcompute関数を実行する。
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.round_number == 4

class Page34(Page):
    pass
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.round_number == 4

class Page35(WaitPage):
    pass
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.round_number == 4

class Page36(Page):
    form_model = 'group'
    form_fields = ['give_amount_5']
    #プレイヤー1がプレイヤー2に渡すポイントを入力する。

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1 and player.subsession.round_number == 5
        #プレイヤー1だけがこのページを表示する。

    @staticmethod
    def vars_for_template(player: Player):  # 1〜4ラウンドの相手の行動履歴を収集
        history = []
        for r in range(1,5):  # ラウンド1〜4
            group = player.in_round(r).group
            give = group.field_maybe_none(f'give_amount_{r}') or cu(0)
            back = group.field_maybe_none(f'back_amount_{r}') or cu(0)
            give_f = float(give)
            back_f = float(back)
            max_return = give_f * C.MULTIPLIER
            percent = (back_f / max_return *100) if max_return > 0 else 0
            history.append({'round':r,'give':give,'back':back,'percent':round(percent,1)})
        return dict(history=history)

class Page37(WaitPage):
    pass
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.round_number == 5

class Page38(Page):
    form_model = 'group'
    form_fields = ['back_amount_5']
    #プレイヤー2がプレイヤー1に返すポイントを入力する。

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 2 and player.subsession.round_number == 5
        #プレイヤー2だけがこのページを表示する。

    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        give = group.field_maybe_none('give_amount_5') or cu(0)
        multi = give * C.MULTIPLIER

        history = []
        for r in range(1, 5):
            group = player.in_round(r).group
            give_r = group.field_maybe_none(f'give_amount_{r}') or cu(0)
            give_f = float(give_r)
            percent = (give_f / 10 *100) if give_f > 0 else 0
            history.append({'round': r, 'give': give_r, 'percent': round(percent,1)})

        return dict(
            give_amount=give,
            multi_amount=multi,
            history=history
        )

class Page39(WaitPage):
    after_all_players_arrive = compute_5
    #全プレイヤーがこのページに到達したらcompute関数を実行する。
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.round_number == 5

class Page40(Page):
    pass
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.round_number == 5

page_sequence = [Page1, Page2, Page3, Page4, Page5, Page6, Page7, Page8,                          #Game1
                 Page9, Page10, Page11, Page12, Page13, Page14, Page15,                           #Game2
                 Page16, Page17, Page18, Page19, Page20, Page21, Page22, Page23, Page24, Page25,  #Game3
                 Page26, Page27, Page28, Page29, Page30, Page31, Page32, Page33, Page34, Page35,  #Game4
                 Page36, Page37, Page38, Page39, Page40]                                          #Game5
