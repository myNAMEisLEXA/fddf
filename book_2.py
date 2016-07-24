d = {
    1: {
        "text": """ Вы быстро идете вперед и вскоре оказываетесь в лесу. Даже странно, что о нем рассказывают столько страшных и невероятных
              историй: таинственный, зачарованный, с множеством ловушек и опасностей. Пока все тихо и спокойно, высокие и могучие деревья
              справа и слева пропускают достаточно солнечного света, дорога прямая и ровная, и вы немного расслабляетесь.
              Тем более что веселое щебетание птиц убеждает в том, что поблизости нет никакой опасности. По крайней мере, пока нет.
              Примерно через три четверти часа вы доходите до развилки. Путь раздваивается. Теперь вам предстоит принять первое решение - какую дорогу выбрать. 
              Вы пойдете: 
              По правой дороге? - 86. 
              По левой дороге? - 110. """,
        "goto": [86, 110]
    },

    51: {
        "text": """Неутомимо бежит вперед дорога, уже несколько часов идете по ней, а ловушек и опасностей все еще не видно.
             Даже появляется надежда, что лес беспрепятственно пропустит вас и скоро покажутся высокие башни Черного замка.
             Неужели вы будете первым, кто доберется до них? А может быть, главные препятствия совсем не в лесу, а в самом замке?
             Задумавшись, чуть было не проходите мимо незаметной тропинки, отходящей налево от дороги. Посмотрев в ту сторону, замечаете,
             что через густую листву невдалеке виднеется белый домик с красной черепичной крышей. Свернете к нему (21) или решите,
             что дорога ведет вас в правильном направлении, и поторопитесь к цели (27)? """,
        "goto": [21, 27]
    },
    52: {
        "text": """Однако стоит вам достать и развязать заплечный мешок, как женщина в ужасе кричит.
              Через незаметную поначалу дверь в комнату врываются Зеленые рыцари во главе с Капитаном.
              Противостоять их натиску вы просто не в силах, и вашей жизни суждено окончиться именно в этих покоях... """,
        "goto": [1, ]
    },
    53: {
        "text": """Вы подходите к правой двери. Она не заперта и, гостеприимно распахнувшись, пропускает вас в комнату.
               Это что-то вроде помещения для охраны, на стенах которого развешаны карты и пергаментные свитки на непонятном языке.
               Вы не успеваете разглядеть обстановку комнаты, потому что из-за стола навстречу вам встают два огромных Орка в полном вооружении.
               Вы оказались прямо перед стражами замка. Что вы сделаете: попробуете с ними поговорить (519) или будете драться (328)? """,
        "goto": [519, 328]
    },
    54: {
        "text": """Вы взбираетесь наверх, но на полпути вдруг понимаете, что странная веревочная лестница напоминает... гигантскую паутину! В ужасе вы начинаете спускаться, но поздно.
               То, что казалось вам логовом или гнездом, оказывается брюхом гигантского паука, и он быстро-быстро начинает подтягивать вас к себе. ПРОВЕРЬТЕ СВОЮ УДАЧУ. Если вы удачливы,
               то 558, если нет, - 618. """,
        "goto": [558, 618]
    },
    55: {
        "text": """Короткая тропинка вскоре выводит на узкую мощеную дорогу. Оглянувшись назад, немало удивляетесь: лес уже успел заботливо спрятать тропинку, так что даже вы уже не в силах сказать,
               где она только что была. Дорога же, напротив, самая обычная, странно только, что лес как будто сторонится ее. Она беззаботно петляет среди холмов, а деревья безмолвно косятся на нее со стороны.
               Куда вы пойдете по дороге - направо (121) или налево (188)? """,
        "goto": [121, 188]
    },
    56: {
        "text": """У вас нет ни одного полезного заклятия. Остается надеяться только на то, что вас выведут из клетки на допрос. Но Барлад Дэрт не интересуется непрошенными гостями.
              Когда Гоблины заканчивают игру, они принимаются за работу. Вы с ужасом обращаете внимание на незамеченную ранее груду кирпичей в углу. Неторопливо, перебрасываясь шуточками и плоскими остротами,
              они начинают замуровывать вас. Конечно, вы пытаетесь уговорить их не делать этого, обещая все, что только возможно. Но слуги чародея не знают жалости - вскоре работа закончена. Вам же суждено прожить еще несколько недель и умереть от голода в подземельях Черного замка,
              так и не выполнив своей миссии. Теперь-то становится понятно, почему никто из смельчаков не вернулся домой... """,
        "goto": [1, ]
    },
    57: {
        "text": """Клубочек катится прямо. Вернитесь на 27 и сделайте самостоятельный выбор, но учтите: если вы свернете, клубочек укатится.""",
        "goto": [27, ]
    },
    58: {
        "text": """Cосуд оказывается скользким, как рыба, и вам только чудом удается не уронить его на пол. Он пуст, но вы можете положить его в заплечный мешок (- 287). Если хотите теперь попробовать взять серебряный сосуд, то 545.
              Если нет, то самое время выйти из комнаты через противоположную дверь - 39. """,
        "goto": [287, 545, 39]
    },
    59: {
        "text": """ Чудом успеваете отскочить, и дерево падает всего в нескольких сантиметрах от вашего плеча. Вы понимаете, что Оборотень просто заманил вас в ловушку, которой удалось избежать только благодаря благосклонности Судьбы. Если торопитесь, можете идти дальше вперед (240),
              если же жажда мести берет верх, стоит свернуть с дороги и сразиться с негодяем, чей силуэт виднеется неподалеку среди деревьев, - 528. """,
        "goto": [528, ]
    },
    60: {
        "text": """Дорога оказывается недлинной, вскоре вы уже видите ее конец и спешите вперед - 181. """,
        "goto": [181, ]
    },
    61: {
        "text": """Вы идете по левому коридору. Неожиданно одна из его стен переходит в решетку. За ней - небольшие каменные помещения, похожие на тюремные камеры. Вы подносите свет к первой из них. За решеткой - павлин. Вы настолько удивлены, что несколько минут стоите в растерянности.
              Кому понадобилось держать павлина в каменном мешке в подземелье?
              Если у вас есть перо павлина, достаньте его, если же нет, посмотрите, кто сидит за следующей решеткой - 147. """,
        "goto": [147, ]
    },
    62: {
        "text": """Вы накладываете заклятие, и медвежонок выздоравливает на ваших глазах. Благодарная медведица тянет вас за собой в угол берлоги. Там на шкуре лисы лежат маленький амулет и красивый пояс.
              Вряд ли стоит демонстрировать жадность, поэтому вы можете взять с собой только одну из трех вещей: либо амулет (457),
              либо пояс (156), либо шкуру (367) или отказаться, вылезти из берлоги и уйти по дороге, ведущей с поляны в глубь леса (44). """,
        "goto": [457, 156, 367,44]
    },
    63: {
        "text": """Медный ключик не подходит к отверстию в люке и ломается (вычеркните его с Листка путешественника).
              Не дожидаясь, пока сюда заглянет кто-нибудь из слуг волшебника, вы уходите - 416. """,
        "goto": [416, ]
    },
    64: {
        "text": """Вы идете по дороге дальше. Начинает смеркаться. Как странно быстро пролетело время. Кажется, что только-только вошел в лес, а уже темно. Хотите поискать убежище на ночь (340) или пойдете вперед, несмотря на усталость: позади и так достаточно опасностей,
              зачем добавлять к ним новые из-за своей беспечности (442)? """,
        "goto": [340, 442]
    },
    65: {
        "text": """Начальник стражи не успевает даже открыть рот, как вы накидываетесь на него с мечом. Но будьте осторожны: ведь вы можете оказаться далеко не единственным посетителем.
              На столе перед вами слишком много бумаг, так что устраивать пожар, используя заклятие Огня, вряд ли будет разумно. Однако заклятие Копии в вашем распоряжении. Кроме того, можете воспользоваться заклятием Ловкости, увеличив свою Ловкость на две единицы, или Слабости, уменьшив на столько же МОЩНОСТЬ УДАРА противника. 
              НАЧАЛЬНИК СТРАЖИ 
              Ловкость 9 Сила 6 
              Если вы победили противника за три Раунда атаки, то 92. Если же нет, - 619. """,
        "goto": [92, 619]
    },
    66: {
        "text": """ 'Так вы и в самом деле встречали Гиену?', - удивляются они. Вы снова недоумеваете: что может быть общего у этого забавного
              разговорчивого животного с разбойниками. Но не спрашивать же их об этом! Тем временем разбойники не только соглашаются отпустить вас,
              ничего не взяв, но и дарят перо аиста (- 28),
              уверяя, что в дороге оно может пригодиться. И кстати, если вы пойдете от их поляны направо, то как раз выйдете к мосту,
              а там и до замка недалеко.
              С этими словами разбойники растворяются в лесу, давая вам возможность подумать, верить их словам или нет, - 46. """,
        "goto": [46, ]
    },
    67: {
        "text": """Правильно, - одобрительно говорит Домик, - это дракон. Ну что ж, вот тебе коготь Дракона. Когда встретишься с ним, покажи ему коготь, и он тебя не тронет".
               И вправду, не успели вы подумать, как это Домик будет вам что-то давать, как прямо у ваших ног падает драконий коготь (- 382), как будто брошенный откуда-то сверху. Вы решаете ничему не удивляться, и слушаете вторую загадку. "Легче легкого, проще простого, но чтобы попасть в замок, нет ничего ценнее".
               Если вы знаете, что это, то проделайте такое же сложение, если нет, придется уходить - 98. """,
        "goto": [382, 98]
    },
    68: {
        "text": """Вдали раздается глухой звон колоколов. "На допрос", - говорит один старик другому. Слава Богу, думаете вы, значит, все-таки не изваяния. Старик встает, отпирает вашу решетку и,
              прицепив к поясу кинжал, а за спину закинув ваш заплечный мешок, выводит вас из камеры - 160. """,
        "goto": [160, ]
    },
    69: {
        "text": """Рыцарь странно смотрит на бронзовый свисток у вас в руках - и отступает в сторону, пропуская вас. Вы делаете шаг вперед,
              но в это время он с силой налегает на какую-то рукоять, торчащую рядом с ним из стены. Вы с ужасом чувствуете, как пол уходит из-под ног,
              и летите в бездну. Воды реки далеко внизу примут ваш труп... """,
        "goto": [1, ]
    },
    70: {
        "text": """Вы подходите к окну и выглядываете наружу. Все еще стоит ночь, и почти ничего не видно,
              кроме черных зубцов стены и силуэтов сторожевых башенок на фоне бархатно-черного звездного неба. Налюбовавшись открывающимся видом,
              можете либо отойти от окна и вернуться в залу (111), либо, воспользовавшись заклятием Левитации, вылететь наружу и посмотреть,
              нет ли еще где-нибудь незапертых окон (273).""",
        "goto": [111, 273]
    },
    71: {
        "text": """ Фигурный ключ, к сожалению, не подходит к отверстию в люке.
              Опасаясь, что вот-вот может появиться кто-нибудь из слуг чародея, вы покидаете домик - 416. """,
        "goto": [416, ]
    },
    72: {
        "text": """ Уже поздним вечером вы выходите на какую-то дорогу. Поищите убежище на ночь (340)
              или пойдете дальше, несмотря на усталость (442)? """,
        "goto": [340, 442]
    },
    73: {
        "text": """Вскоре еще одна развилка. Сколько же можно, думаете вы, так ведь недолго и заблудиться и вообще никогда не выйти к замку,
              а только плутать всю жизнь по этим дорогам и тропинкам.
              Но так или иначе, а выбор делать надо. Свернете на дорогу, которая идет налево (286), или пойдете дальше (646)?""",
        "goto": [286, 646]
    },
    74: {
        "text": """ Донжон - главная башня замка - совсем рядом. В сердце цитадели ведут большие массивные двери,
              к которым подвешен дверной молоток в форме боевого топора - 257. """,
        "goto": [257, ]
    },
    75: {
        "text": """ Только меч Зеленого рыцаря может сразить Каменных крыс. Увидев его, они в ужасе разбегаются.
              Ваш путь свободен. Дверь справа от вас ведет в следующую комнату - 480""",
        "goto": [480, ]
    },
    76: {
        "text": """Дверь открывается, и вы попадаете на кухню. На огромных плитах в котлах что-то варится. Кажется, повар и два поваренка
              совсем не удивлены вашим появлением: они заняты стряпней. В углу кухни виден какой-то сундук, которого здесь явно быть не должно,
              настолько странно он смотрится. Рядом с ним дверь, через которую вы можете выйти (379). Но, если хотите, можете сначала поговорить с поварами (486).
              Вряд ли разумно сразу совать свой нос в сундук, даже если вам безумно любопытно, что там: ведь на кухне есть посторонние. """,
        "goto": [379, 486]
    },
    77: {
        "text": """Лошадь всегда чувствует неумелого наездника - она легко сбрасывает вас и уносится в лес. Вы же с размаху падаете на землю (потеряйте от боли 2 СИЛЫ).
              К тому же вам лучше поторопиться уйти, ведь если появится хозяин коня, он вряд ли скажет вам спасибо - 378. """,
        "goto": [378, ]
    },
    78: {
        "text": """Вы попадаете в абсолютно пустую комнату. Из нее только одна дверь, но она наглухо закрыта и не поддается, как бы ни старались ее открыть.
              Если у вас есть еще одно заклятие Левитации, используйте его либо для того, чтобы вернуться обратно (111), либо для того, чтобы влететь
              в окно немного ниже (566). Иначе остается только позвать Пегаса. Если вы и этого не можете сделать, то через несколько часов стены комнаты
              раскалятся и сдвинутся, а вам придется, по возможности не теряя спокойствия, смотреть на это и торопить смерть... """,
        "goto": [111, 566]
    },
    79: {
        "text": """  Вы кидаете женщинам 1 золотой, из-за которого начинается драка.
              Жадность вас подвела, и теперь остается только один выход: быстро выбежать в следующую дверь,
              что вы и делаете, попадая в какой-то коридор - 251.  """,
        "goto": [251, ]
    },
    80: {
        "text": """Дверь в конце маленького коридорчика ведет на лестницу. Охраны поблизости нет, дверь не заперта. Вы открываете ее - 322. """,
        "goto": [322]
    },
    81: {
        "text": """Клубочек катится прямо, а вы можете вернуться на 51 и самостоятельно сделать выбор, куда вам лучше пойти.
              Но учтите: если вы свернете, клубочек укатится прочь, и дальше вам придется обходиться без него. """,
        "goto": [51, ]
    },
    82: {
        "text": """Вы продолжаете идти дальше. Вдруг ваше внимание привлекает какое-то движение в листве большого клена, стоящего справа от дороги.
              Остановившись, поднимаете голову. Из листвы на вас смотрит умное лицо с маленькой аккуратной бородкой. Большие серые глаза внимательно
              изучают вас какое-то время, а потом вниз спрыгивает маленький старичок в зеленой курточке и аккуратных зеленых штанишках,
              заправленных в сапожки. Это Лесовичок, охраняющий дорогу. Но от кого: от ваших врагов или от ваших друзей? Этого-то вы и не знаете, а между тем Лесовичок спрашивает,
              кто вы. Вы отвечаете, что вы - одинокий искатель приключений, которого судьба занесла в Зачарованный лес. Однако он не успокаивается и интересуется,
              что вы ищете в этом лесу. Теперь уже туманными неопределенностями не отделаться. Что вы ответите: что идете в Черный замок сражаться с волшебником (610),
              что идете туда освобождать Принцессу (284), что забрели в лес случайно (492), или решите, что он не имеет права задавать вам никаких вопросов - и обнажите меч (563)? """,
        "goto": [610, 284, 492]
    },
    83: {
        "text": """Вы пытаетесь отступить назад и захлопнуть дверь, но скелет не дает вам это сделать. Несмотря на то, что он только ранил вас,
              когда вы повернулись к нему спиной (потеряйте 2 СИЛЫ), бегство не удалось. Вам придется вернуться на 247 и сразиться с ним. """,
        "goto": [247]
    },
    84: {
        "text": """Вы входите в саркофаг со статуей Короля. Внутри еще одна статуя: Король, сидящий на троне. На его шее на золотой цепи
              висит что-то вроде медальона с золотым изображением орла, уносящего в когтях свою добычу. В осанке Короля столько величия,
              что вы можете представить его только во главе огромного и могущественного государства. Орел - герб Катэны, так что это
              скорее всего Свен Айрин II, захороненный еще в те дни, когда население Двэлла переживало Эпоху Единства. Однако дни
              его великой славы остались в прошлом. Теперь же вы можете снять с шеи Короля медальон с орлом (- 72) и взять его с собой.
              Одолеваемый думами о Королях и Лордах былых времен, выходите из саркофага. Пронизывающее воздух напряжение не позволяет
              задерживаться: все в вас стремится прочь от этого места. Через какую из дверей вы покинете подземную усыпальницу: через правую (547) или через левую (501)? """,
        "goto": [72, 547, 501]
    },
    85: {
        "text": """На несколько секунд замерев, внимательно прислушиваетесь. За одной из дверей раздается громкий топот Гоблинов. Вы наугад дергаете ручку одной из дальних дверей - 398. """,
        "goto": [398]
    },
    86: {
        "text": """Дорога широка и удобна. По ней явно ходят чаще, чем по той, что отходила влево. Следы копыт в пыли говорят о том,
              что совсем недавно здесь проезжали всадники, и вы уже жалеете, что поверили сказам об ужасах Зачарованного леса и не отправились
              в путь верхом. Вот и развилка: наезженная дорога немного поворачивает влево и скрывается в лесу, другая, поуже,
              менее удобная и утоптанная, отходит от нее направо. Куда вы пойдете? 
              Налево? - 530. 
              Направо? - 403.""",
        "goto": [530, 403]
    },
    87: {
        "text": """Вы произносите заклятие и готовитесь взлететь, но... ничего не происходит. Волшебник надежно защитил свой замок от непрошенных магов.
              Однако заклятие истрачено (вычеркните его) и отправляйтесь дальше в обход замка - 533""",
        "goto": [533, ]
    },
    88: {
        "text": """Поле кончается, впереди заросли малогостеприимного низкого кустарника. Мысль о том, что придется через него продираться,
              не доставляет вам ни малейшего удовольствия. Ну так что же? 
              Пойдете через кустарник? - 177. 
              Или свернете к озеру? - 212.""",
        "goto": [177, 212]
    },
    89: {
        "text": """Деревья, растущие по краям тропинки, закрывают почти весь свет, идти приходится медленно и осторожно. Внезапно вы чувствуете,
              что сзади на вас кто-то смотрит, и хотя никаких шагов слышно не было, медленно оборачиваетесь.
              Посреди дороги стоит невысокий человек в потрепанной крестьянской одежде. Он небрит и оброс, в глазах - голодный блеск.
              За спиной слышится легкий шум, и краем глаза вы видите, что из леса выходит еще один человек, одетый так же, как и первый,
              но немного повыше ростом и пошире в плечах. Теперь и вперед дороги нет. Оба медленно приближаются к вам, и решение надо
              принимать как можно быстрее. Попробуете поговорить с ними и убедить в том, что вы не желаете им зла (419), предложите им еду в знак своих мирных намерений (104) или будете драться (374) ? """,
        "goto": [419,104]
    },
    90: {
        "text": """К сожалению, дверь не поддастся, даже если вы постараетесь ее выломать. А вам придется попытаться это сделать: потолок начинает
              медленно опускаться. Если не удастся открыть дверь,
              то жить вам осталось всего несколько минут: комната-западня выполнит свое предназначение... """,
        "goto": [1, ]
    },
    91: {
        "text": """Вы просите накормить вас. Повар соглашается, но требует за это плату - 2 золотых. Если согласны, то 621, если нет,
              то уходите - 379. Однако если вас крайне заинтересовал сундук,
              не остается иного выхода, кроме как убить повара и его подручных и удовлетворить свое любопытство - 604.""",
        "goto": [621, 379, 604]
    },
    92: {
        "text": """Начальник стражи со стоном падает на пол у ваших ног. Он мертв. На первый взгляд в комнате нет совершенно ничего интересного.
              Решив не проверять, слышал ли кто-нибудь шум схватки, выходите в дверь по ту сторону стола и плотно прикрываете ее за собой - 39. """,
        "goto": [39, ]
    },
    93:  {
        "text": """Заклятия вам не помогут: она слишком искусная колдунья, чтобы ее можно было удивить иллюзией или копией. 
              ЖЕНЩИНА-ВАМПИР 
              Ловкость 11 Сила 14 
              Если вы победили ее, то, осмотрев комнату повнимательнее, обнаруживаете дверь, скрытую за портьерой слева от вас - 301. """,
        "goto": [301, ]
    },
    94: {
        "text": """Все правильно, и Лев впускает вас - 265""",
        "goto": [265, ]
    },
    #strange
    95: {
        "text": """Домик доволен вашей сообразительностью "Ну что ж, - говорит он, - раз так, храбрый путешественник, то я скажу тебе пароль, чтобы попасть в замок.
              Пароль - "Хобгоблин".(Когда вам понадобится пароль, вычтите 197 из номера параграфа, на котором будете тогда находиться.)
              "А теперь - последняя загадка. Если убьешь на поединке чужеземного рыцаря, о себе не напомнит и сон твой не нарушит. Если же друга предашь,
              разговорами замучит, пожалеешь, что родился". Если знаете отгадку,
              поступите с ней так же, как и с предыдущими: прибавьте к результату 50 и посмотрите нужный параграф. Если же нет, то придется уходить - 98.""",
        "goto": [1, ]
    },
    96: {
        "text": """Огненный шар попадает стражу прямо в грудь и прожигает латы.
              Он мертв, вы же торопитесь дальше по коридору, пока дорогу не преграждает дверь - 241""",
        "goto": [241, ]
    },
    #strange
    97: {
        "text": """Вы решаете идти по дороге дальше, не обращая внимания на ощущение некоторой опасности, исходящее от этого узкого прохода.
              Но вскоре понимаете, что иногда все же стоит доверять своим предчувствиям. Слышится шум обвала, и с вершин обоих холмов вниз
              начинают катиться огромные валуны. Но откуда они там взялись? Вы готовы поклясться, что еще несколько минут назад их там не было.
              Так и есть: это ловушка! Теперь остается надеяться только на Судьбу.
              ПРОВЕРЬТЕ СВОЮ УДАЧУ. Если удачливы, то 622, если же нет, - 306""",
        "goto": [622, 306]
    },
    98: {
        "text": """Судя по всему, дорожка идет в правильном направлении. Вы чувствуете, как вокруг сгущаются сумрак и беспокойство,
              словно вы потревожили какую-то неумолимую силу, которая не замедлит нанести ответный удар. Но вот лес, доставивший
              столько неприятностей, кончается, и вы выходите на странную огромную поляну. Деревья по ее краям повалены и обуглены,
              однако задуматься о причине этого вы не успеваете - 412""",
        "goto": [412, ]
    },
    99: {
        "text": """Тропинка не сулит вам ничего хорошего: понемногу ноги начинает засасывать, сначала вы идете вперед через силу,
              потом, осознав всю тщетность этого, поворачиваете назад с надеждой выбраться из западни. Но не тут-то было.
              Под ногами - мерзкое, засасывающее болото, обрадованно чавкающее, почуяв очередную жертву. Через несколько минут все кончено,
              и лишь заплечный мешок, зацепившийся за одно из склонившихся над трясиной деревьев, напоминает о смелом,
              но неосторожном путешественнике...""",
        "goto": [1, ]
    },
    100: {
        "text": """Вы оказываетесь во дворе Черного замка. Яркий свет факелов прямо перед вами заставляет остановиться и спрятаться
              в нише ворот. Двор полон Гоблинами и Орками, снующими между палаток, тут и там горят костры.
              Вы чуть было не оказались в самом центре военного лагеря врага. За палатками, в центре двора, виднеется большое мрачное строение.
              Судя по всему, это и есть цель вашего путешествия. Как ни странно, река течет и здесь - справа от вас.
              При мерцающем свете видно, что вода уходит под землю где-то неподалеку от центрального здания. Вам надо решать, куда держать путь. 
              К реке? - 375. 
              К палаткам? - 424.""",
        "goto": [375, 424]
    }
}








    