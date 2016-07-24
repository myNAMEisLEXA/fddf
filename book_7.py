d={
	"301":{
	"text":
'''Узкая длинная комната переходит в широкую парадную лестницу, поднимающуюся наверх.
У подножия лестницы четыре больших деревянных кресла: три слева и одно, чуть на отшибе, справа.
Резная спинка правого кресла украшена большой золотой короной. 
В креслах - Зеленые рыцари. 
На них нет ни шлемов, ни тяжелых лат, только легкие панцири и мантии с вышитым на них силуэтом Черного замка. 
Рыцарь, сидящий в кресле с короной, очевидно, Капитан. 
Склонив голову немного набок, он указывает на вас двум другим. 
Они встают с кресел и медленно приближаются. С лязгом, от которого холодеет кровь, мечи вылетают из ножен. 
Сердце учащенно бьется: вы понимаете, что наконец-то добрались до сердца цитадели. 
Если у вас есть Оберег или серебряный сосуд, можете попытаться воспользоваться ими. Иначе - 628. ''',
	"goto": [628]
},
	"302":{
	"text":'''Вы подходите поближе и склоняетесь над умирающим. 
"Я знаю, что мне недолго осталось жить, - говорит он. - И ты ничем не можешь мне помочь. 
Прошу тебя только об одном: облегчи мои страдания. 
Дай мне напиться из твоей фляги". Что вы сделаете? 
 Дадите умирающему напиться? - 11. 
 Откажете и пойдете дальше? - 629.''',
      "goto": [11,629]
},
	"303":{
	"text": '''Лес редеет, тропинка в траве почти незаметна, под ногами попадается все больше и больше мха. 
Чувствуется, что почва становится все мягче и мягче, идти удается с большим трудом, земля засасывает. 
Но тропинка уверенно бежит вперед, и вы можете либо идти по ней дальше (99), 
либо вернуться на развилку и пойти направо (117). ''',
	"goto": [117,99]
},
	"304":{
	"text": '''Тропинка покидает лес и идет по непаханому полю неподалеку от опушки. 
Вы начинаете понимать, что вряд ли пошли в правильном направлении: 
ведь Черный замок должен быть в самом сердце леса. 
Оглядевшись вокруг, замечаете, что слева осталась лишь тонкая полоска деревьев, 
за которой мерцает, переливаясь на солнце, большое озеро. 
 Пойдете дальше - 88, 
 свернете к озеру - 12.''',
      "goto": [12,88] 
},
	"305":{
	"text": '''Тропинка становится все шире и шире и превращается в большую дорогу.
Вы недоумеваете: кому это пришло в голову посреди чащобы проложить такой путь. 
Быть может, дорогу просто не достроили? 
Но это останется одной из загадок Зачарованного леса, которую вам вряд ли суждено разгадать. 
Конец дороги уже виден: она выходит на огромную поляну. 
Деревья по ее краям повалены и обуглены, кажется, недавно здесь бушевал пожар. 
На безлюдную поляну выходит еще несколько таких же широких дорог - 412.''',
	"goto": [12,88] 
},
	"306":{
	"text": ''' Последнее, что вы увидите в этой жизни, 
будет громадный черный валун, настигающий вас, и буквы Б и Д, 
горящие на нем недобрым зеленым пламенем и закрывающие от вас небо...''',
},
	"307":{
	"text": '''Вы наполняете флягу. 
В будущем можете использовать эту воду так же, как и ту, что была с собой.
Потом, внимательно глядя по сторонам, идете дальше по главной улице - 161. ''',
	"goto": [161] 
},
	"308":{
	"text": '''Вы приближаетесь к центральному строению, 
и сторожка перестает загораживать длинное низкое здание в глубине двора. 
Это или сарай, или конюшня. В то же время внимание все больше и больше привлекает река. 
Может быть, с ее помощью можно проникнуть под цитадель незамеченным? 
Или стоит переплыть ее и осмотреть ту часть двора, которая сейчас не видна? 
Куда же вы направитесь? 
  К центральному строению? - 416. 
  К низкому зданию справа? - 386. 
  К реке? - 4.''',
	"goto": [416, 386, 4] 
},
	"309":{
	"text": '''На дороге появляется скачущий во весь опор рыцарь. 
На нем тяжелые зеленые латы, в руке - копье, на щите - силуэт огромного Черного замка, а чуть слева и пониже - голубая змейка. 
Вы не можете оторвать взгляд от щита, изображение начинает расти, 
и в какой-то момент появляется ощущение, что вы стоите прямо перед этим замком, а змейка превращается в широкую реку, исчезающую под одной из угловых башенок... 
Резкая боль заставляет прийти в себя. Вы понимаете, что Зеленый рыцарь просто-напросто загипнотизировал вас волшебным щитом, а теперь, ударив копьем (потеряйте 3 СИЛЫ) и отбросив его, на полном скаку разворачивается, вынимая из ножен меч. 
Если хотите попытаться убежать, не медлите (481). Иначе - сражайтесь: пытаться наложить какое-нибудь заклятие уже поздно. 
      ЗЕЛЕНЫЙ РЫЦАРЬ 
 Ловкость 10 Сила 10 
 Если вы победили его, то 126. Но учтите, 
 каждый раз вам придется вычитать из вашей МОЩНОСТИ УДАРА 1, ведь он бьется на коне, а вы нет. ''',
	"goto": [416, 386, 4] 
},   
	"310":{
	"text": '''Старик радостно улыбается и говорит, 
что, хотя он и не надеется дожить до того дня, когда силы Зла будут низвергнуты, 
но с радостью поможет отважному путешественнику. Он рассказывает, 
что дорога пойдет мимо гибельных Коричневых топей, поэтому на первой развилке сворачивать с нее ни в коем случае нельзя: 
болото не выпускает своих жертв. Кроме этого он предупреждает, что самые страшные и отважные воины среди слуг волшебника - Зеленые рыцари. 
Они не только смело сражаются, но и мало кто оказывается в силах противостоять их натиску. 
Барлад Дэрт передал им частицу своего мастерства, и теперь они не менее искусно развеивают многие заклятия врага, но успешнее всего - заклятие Копии. 
Недоумевая, откуда старик про все это знает, вы благодарите его и отправляетесь дальше - 179.''', 	
	"goto": [179] 
},
	"311":{
	"text": '''Когда она видит зеркальце, то поначалу с интересом берет незнакомый предмет. 
Но стоит женщине взглянуть в него, как ее лицо искажается злобой. 
Изящная вещица летит на пол и разбивается вдребезги. 
Кажется, вам все же придется драться - 93.''', 
	"goto": [93] 
},    
	"312":{
	"text": '''Вам удается построить плот, но после этого чувствуете себя совершенно выдохнувшимся и измочаленным 
(потеряйте 3 СИЛЫ) от непривычной работы. 
Однако вы вполне благополучно пересекаете озеро, 
хотя на противоположном берегу поджидает еще один сюрприз - 192. ''',
	"goto": [192] 
},
	"313":{
	"text": '''Заклятие действует успешно, и вы без приключений переплываете реку - 222. ''', 
	"goto": [222] 
},  
	"314":{
	"text": '''Накладываете заклятие Слабости - и действительно слабеете. 
Вы - а не рыцари! Они, не долго думая, направили магию обратно. 
Теперь деритесь с ними, но уменьшайте на 2 МОЩНОСТЬ своего УДАРА - 183. ''', 
	"goto": [183] 
},
	"315":{
	"text": '''Вы поворачиваетесь к Начальнику стражи и говорите: 
"Мне поручили передать вам...", однако фраза так и остается незаконченной. 
Глаза Гоблина лезут на лоб, а рука тянется к звонку. 
Всего через мгновение комната наполняется вооруженными Орками. 
Вы пытаетесь сопротивляться, но один из стражников, подкравшись сзади, 
бьет вас своим мечом плашмя по голове (потеряйте 2 СИЛЫ). Вы теряете сознание... - 409. ''', 
	"goto": [409] 
}, 
	"316":{
	"text": '''Вы достаете меч и нападаете на Дракона. Дохнув пламенем (потеряйте 4 СИЛЫ), он бросается в бой. 
      ДРАКОН 
 Ловкость 12 Сила 8 
Кстати, обнаружив, что перед вами столь сильный противник, 
можете воспользоваться заклятием Копии. Если удастся дважды ранить Дракона, то 513.''', 
	"goto": [513] 
},
	"317":{
	"text": '''Решившись, показываете кольцо. В ответ он рассказывает, 
что некогда был одним из трех волшебников, живших в лесу до появления Барлада Дэрта. 
Его имя Хэрнок. Когда пришли тяжелые времена, он, единственный из трех, объявил войну магу. 
И потерпел неудачу. Серебряное кольцо - символ власти и мудрости - было похищено, 
а сам он брошен в эту подземную тюрьму. Неудивительно, что старик умоляет вернуть кольцо. 
Сделаете это (127)? Или откажетесь и посмотрите, кто сидит в соседней клетке (225)? ''', 
	"goto": [127, 225] 
},
	"318":{
	"text": '''Без труда откинув крышку ларя, достаете большой металлический ключ. 
На нем выгравировано: "Все". Этот ключ поможет вам открыть многие запертые двери в замке.
 Если какая-то дверь не открывается обычным способом, попробуйте вычесть 40 из номера параграфа, 
 на котором вы будете, - вдруг ключ и подойдет. Но сейчас вам надо торопиться и уходить - 193.''', 
	"goto": [193] 
},
	"319":{
	"text": '''Ворота хорошо охраняются. Возле них стоят три Орка, 
подозрительно оглядывающие вас с ног до головы. 
Вы понимаете, что легко проникнуть в замок не удастся. 
Если знаете пароль, воспользуйтесь им, если же нет, то придется на ходу придумать, 
что им сказать. Будете утверждать, что вы бродячий торговец и идете в замок торговать (31), 
что вы азартный игрок и идете развлекать волшебника (439) или что вы собираетесь наняться в армию чародея (146)? 
Иначе придется драться - 428. ''', 
	"goto": [31, 439, 146, 428] 
},
	"320":{
	"text": '''Вы заходите за угол. Прямо перед вами - Зеленый рыцарь. 
На его щите сверкает баронская корона, а меч направлен прямо на вас. 
"Пропуск!" - глухо говорит он из-под забрала. 
Рискнете предложить что-то в виде пропуска или атакуете его? Если первое, то 355, 
если второе, - 543. Кроме того, можете, если хотите, попытаться воспользоваться серебряным сосудом. ''', 
	"goto": [355, 543, 263] 
},
	"321":{
	"text": '''Дух мертвых, который зорко охраняет могилы, пробудился. 
Теперь придется драться с ним. Попробуете наложить какое-нибудь заклятие (640) 
или будете сражаться мечом (247)?''', 
	"goto": [640, 247] 
},   
	"322":{
	"text": '''Поднявшись по лестнице, попадаете в маленькую прихожую. 
Наверняка до цели уже недалеко: обстановка здесь гораздо богаче и роскошней,
странно только, что у дверей нет охраны. 
Справа от входа - огромное окно, в стенах - напротив и справа - двери. 
В какую дверь вы пойдете? Прямо (277) или направо (556)?''', 
	"goto": [277, 556] 
},  
	"323":{
	"text": '''Вы открываете дверь и входите в очень странную комнату. 
Она абсолютно пуста: голые стены, никакой мебели. 
Из комнаты ведут три двери, в одну из которых вы только что вошли. 
Неожиданно от стены отделяется маленькая сгорбленная старушка. 
Сначала вы не заметили ее, да и была ли она здесь? 
Медленно приближаясь к вам, она протягивает руку, как бы прося милостыню. 
Что вы сделаете? Предъявите пропуск, замахнетесь на нее мечом (522), 
дадите ей денег (137) или предложите какой-нибудь подарок (194)?''', 
	"goto": [522, 137, 194] 
},
	"324":{
	"text": '''Когда вы склоняетесь над Принцессой, 
свет свечи падает на рубин перстня, и камень оживает. 
Вам кажется, что от него начинает исходить тепло, однако само кольцо остается совсем холодным... 
О, чудо: тепло от перстня не только согревает Принцессу, но и будит ее! 
Она глубоко вздыхает и, приоткрыв глаза, приподнимается на кровати. 
Оглядевшись из-под полуопущенных век, Принцесса спрашивает, жив ли еще ее тюремщик, ненавистный Барлад Дэрт? 
К счастью, вы можете ее порадовать: чародей мертв - 655. ''', 
	"goto": [655] 
},
	"325":{
	"text": '''Вам повезло: вы не только оказались в Черном замке, но у вас есть еще с собой латы Зеленого рыцаря. 
Перед каждой дверью вы имеете право решить, хотите войти в нее в латах или нет. 
Однако, если надумаете переодеться, учтите, что такая возможность доступна только в пустой комнате. 
Если латы оказываются на вас, прибавьте 60 к номеру параграфа, на который будет вести дверь. 
В том случае, если одежда будет играть хоть какую-нибудь роль, вы прочтете, что случится, когда вы захотите выдать себя за рыцаря. 
Если нет, это будет самый обычный параграф, не имеющий никакого отношения к вашим приключениям. 
Теперь же вернитесь на 265 и идите дальше. ''',
	"goto": [265] 
},
	"326":{
	"text": '''	ВОДЯНОЙ 
 Ловкость 9 Сила 8 
Если вы победили его, то 573. Если хотите, во время боя можете покинуть таверну и бежать - 504. ''', 
	"goto": [573, 504] 
},
	"327":{
	"text": '''Это какой-то неправильный Дракон. 
Драгоценности его мало интересуют, и он недвусмысленно дает вам это понять, 
выдохнув струю пламени (потеряйте 2 СИЛЫ). Теперь вам придется драться - 316. ''', 
	"goto": [316] 
},
	"328":{
	"text": '''Пока Орки не успели понять, в чем дело, вы нападаете на них. 
    ПЕРВЫЙ ОРК 
 Ловкость 8 Сила 8 
    ВТОРОЙ ОРК 
 Ловкость 7 Сила 8 
Сражаться с ними придется одновременно. 
Если хотите, можете воспользоваться заклятиями Копии, Ловкости или Слабости 
(в последних случаях можете либо увеличить на время боя на 2 свою Ловкость, 
либо ослабить на столько же МОЩНОСТЬ УДАРА одного из противников). Если убили обоих врагов за 8 раундов атаки, то 505. Если нет, то 248.''', 
	"goto": [316] 
},
	"329":{
	"text": '''Тропинка спускается на дно неглубокого оврага. 
Над вами по мосту проходит дорога, но склоны оврага слишком круты, чтобы можно было взобраться на нее. 
Через некоторое время вы подходите к крепкому бревенчатому дому, и тропинка заканчивается у его дверей - 33. ''', 
	"goto": [33] 
},
	"330":{
	"text": '''Тропинка спускается на дно неглубокого оврага. 
Над вами по мосту проходит дорога, но склоны оврага слишком круты, чтобы можно было взобраться на нее. 
Через некоторое время вы подходите к крепкому бревенчатому дому, и тропинка заканчивается у его дверей - 33. ''', 
	"goto": [33] 
},
	"331":{
	"text": '''Она смотрит на вас как на сумасшедшего и с негодованием ломает стрелу. 
Подарок ей явно не понравился. Можете теперь либо попробовать откупиться (137), либо вынуть меч и драться (522).''', 
	"goto": [137, 522] 
},
	"332":{
	"text": '''Дорога от таверны ведет прямо в лес, и вы радуетесь, что наконец-то идете в нужном направлении. 
Невысокий подлесок вновь сменяется древними могучими деревьями. Интересно, кто же все-таки проложил здесь все эти дороги и тропы? 
Неужели неутомимые воины Барлада Дэрта? Или они существовали задолго до них? Так или иначе вы замечаете, что заброшенных тропинок пока что не попадается: по всем ходят много и часто. 
Погруженный в свои мысли, доходите до развилки. Ваша дорога идет прямо, другая отходит от нее налево. Но куда направитесь вы? 
 Прямо? - 250. 	
 Или налево? - 461. ''', 
	"goto": [250, 461] 
},
	"333":{
	"text": '''Тропинка выводит к маленькому домику, стоящему посреди поляны. 
Трудно даже предположить, кто может жить в такой крошечной хижине. 
Вероятно, или гномы, или карлики. Но когда вы собрались наклониться и заглянуть в окошечко 
(домик в половину вашего роста), как вдруг откуда-то слышится голос: "Поговори со мной, храбрый путешественник". 
"Но кто ты?", - оторопело спрашиваете вы. "Я - Лесной домик", - слышится в ответ. С вами говорит сам домик! 
Ну так что, поговорите с ним (149) или пойдете дальше по дорожке, ведущей прочь (98)?''', 
	"goto": [149, 98] 
},
	"334":{
	"text": '''Вы проходите через сад, и тропинка, петляя, уходит в лес - 99.''', 
	"goto": [99] 
},
	"335":{
	"text": '''Обшарив одежду разбойников, находите 7 золотых, перо аиста (- 28) и бронзовую статуэтку богини смерти Орробы (+ 109). 
Можете взять с собой все, что считаете нужным, и идти дальше - 46.''', 
	"goto": [46] 
},
	"336":{
	"text": '''Немного подумав, решаете все же сорвать золотой апельсин (+ 200). 
Вокруг все тихо - ничего особенного не происходит. Теперь можете покинуть остров. 
А кроме того, бросить кубик и почистить соответствующий квадрат УДАЧИ - 24.''', 
	"goto": [24] 
}, 
	"337":{
	"text": '''Вы оказываетесь в комнате Начальника стражи. 
Гордый и важный Гоблин, с надутыми щеками, в расшитом золотыми галунами плаще, на котором вышиты буквы "Б" и "Д", 
он сидит за столом и очень удивлен, увидев вас. 
Попробуюте подкупить его (613), поговорить с ним (249) или будете драться (65)?''',
	"goto": [613, 249, 65] 
}, 
	"338":{
	"text": '''Дорога начинает петлять, вы скоро запутываетесь в ее поворотах и перестаете понимать, в каком направлении идете. 
Тем временем смеркается. Не чувствуя особенной опасности (зато чувствуя сильную усталость), 
ночуете прямо на обочине (благо ночи еще стоят теплые) и продолжаете путь с первыми лучами солнца. 
За ночь дорога не стала вести себя лучше: сначала она подходит к самой опушке леса, но потом опять устремляется в чащу.
Наконец перед вами два пути: направо (151) и прямо (231). Какой из них вы изберете? ''', 
	"goto": [151, 231] 
},
	"339":{
	"text": '''Если вы действительно уже встречали кого-то из их знакомых, 
то сложите порядковые номера букв, составляющих его имя, прибавьте к этому 30 и посмотрите параграф с получившимся номером. 
Если же вы сказали неправду, то обман непременно откроется, и уж лучше самому начать бой - 123. ''',
	"goto": [123] 
},
	"340":{
	"text": '''Неподалеку в лесу виднеется шалаш. Он давно заброшен, но может служить прекрасным местом для ночлега. 
Положив меч рядом, вы чутко спите, но ночь проходит спокойно. Можете восстановить 2 СИЛЫ и отправляйтесь в путь с рассветом - 509. ''',
	"goto": [509] 
},
	"341":{
	"text": '''Если воспользуетесь заклятием Ловкости, можете на время боя увеличить на 2 свою Ловкость. 
Предпочтете заклятие Слабости, вычитайте 2 из МОЩНОСТИ УДАРА любого из стражников. 
Коли выбрали эти магические приемы или решили просто сражаться мечом, - 487. 
Если же есть желание обратиться к заклятию Огня, то 506. ''', 
	"goto": [487, 506] 
},
	"342":{
	"text": '''Вы идете по дороге всю ночь. К сожалению, приходится миновать несколько перекрестков, но в темноте вы не рискуете сворачивать с намеченного пути. 
Начинает сказываться усталость, глаза слипаются (потеряйте 3 СИЛЫ). Но когда из-за деревьев робко встает солнце, вы видите, что конец дороги близок - 181. ''', 
	"goto": [181] 
},
	"343":{
	"text": '''Вы показываете пропуск, и она тает в воздухе. Кажется, еще одного стража удалось миновать вполне благополучно. 
Но в комнате две двери, в какую из них пойти? Прямо (252) или направо (542)?''', 
	"goto": [252, 542] 
},
	"344":{
	"text": '''Вы быстро накладываете еще одно заклятие Огня, и оно поражает вторую голову Дракона. 
Вам повезло: неутомимый страж мог причинить вам немало неприятностей - 454.''', 
	"goto": [454] 
},
	"345":{
	"text": '''Библиотекарь говорит, что попробует найти что-нибудь подходящее, и скрывается за полками - 649.''', 
	"goto": [649] 
},
	"346":{
	"text": '''Вы очнулись в каменном мешке. На стенах - сырость, маленькое окошко в двери забрано крупной решеткой. 
Это тюрьма для особо опасных преступников. Голова почти прошла, и вы подходите к окошку. 
При слабом свете свечи, горящей где-то снаружи, видно, что по обеим сторонам двери стоят каменные табуреты. 
На них неподвижно сидят два старика. Вы даже не можете понять, статуи это или живые люди. 
Хотите воспользоваться каким-нибудь заклятием, чтобы выбраться отсюда (153), или посмотрите, что будет дальше (68)?''', 
	"goto": [68, 153] 
},
	"347":{
	"text": '''К вашему ужасу и изумлению, голова у Дракона отрастает вновь. Вам не суждено победить его - он спалит вас огнем быстрее, чем вы сможете решить, что же делать. 
А жаль, ведь башни Черного замка уже видны сквозь деревья...''', 
},
	"348":{
	"text": '''Коридор приводит к двери. Она не заперта, и когда вы открываете ее, то видите лестницу, ведущую вниз. Вы спускаетесь по ней - 544.''', 
	"goto": [544] 
},
	"349":{
	"text": '''Банан резко меняет настроение Обезьяны. Она съедает его и проникается к вам нескрываемой симпатией. 
А кроме того, в ответ тоже дарит подарок: изящный гребень из слоновой кости (- 255). 
После этого вы некоторое время отдыхаете в тени (можете восстановить 1 СИЛУ), но вскоре Обезьяна начинает нетерпеливо дергать вас за рукав. 
Как бы подавая пример, она бежит вперед по тропинке, ведущей к лесу, и явно зовет за собой. 
Когда вы подходите поближе, то видите, что она отнюдь не собирается входить в лес по тропинке, а манит вас куда-то в сторону. Пойдете за ней (615), по тропинке (305) или вернетесь на дорогу (210)?''', 
	"goto": [615, 305, 210] 
},
	"350":{
	"text": '''Крестьянин внимательно смотрит на вас и говорит, что может проводить к человеку, который вам нужен. Через несколько домов живет торговец, поставляющий в Черный замок сено для лошадей волшебника. 
Тот за небольшую плату (3 золотых) соглашается спрятать вас на одном из возов под сеном и доставить в замок. Примете его предложение (574) или откажетесь и покинете деревню по одной из дорог: на юг (235) или на запад (2).''', 
	"goto": [574, 235, 2] 
},
}