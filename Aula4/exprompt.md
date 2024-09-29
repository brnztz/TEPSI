## Exercícios

Para consolidar os conceitos apresentados, aqui estão alguns exercícios práticos para você aplicar as técnicas básicas da engenharia de prompts. 

Para cada exercício anote o prompt inicial e a resposta obtida, o prompt final (que lhe agradou) e a resposta obtida. Segue modelo

Prompt:
```d
O Céu é
```

Saída:
```d
Azul
```

---

1. Crie um prompt simples pedindo ao modelo para escrever uma carta de recomendação sem fornecer nenhum contexto adicional. Depois, revise o prompt adicionando detalhes sobre o destinatário e o propósito da carta. Como o contexto influenciou a qualidade da resposta?

Prompt:
```d
Escreva uma carta de recomendação.
```

Saída: 
```d
Aqui vai um exemplo de carta de recomendação:

[Cabeçalho da empresa/Instituição]

[Seu Nome]
[Seu Cargo/Ocupação]
[Data da carta]

[Endereço da empresa/Instituição]
[País/Cidade]

[Cidade, País de destino]
[Endereço do destinatário]

[Destinatário's Name]
[Destinatário's Cargo/Ocupação]

Estimado(a) [Destinatário's Name],

Eu, [Seu Nome], estou escrevendo para expressar meu mais alto reconhecimento e respeito ao [nome do nominado], que foi meu [ professor/colega/colaborador] por [ perímetro de tempo]. No tempo que trabalhamos juntos, eu tive a oportunidade de observar e experimentar [nome do nominado]'s habilidades e característica para liderança, criar equipes, comunicação e resolução de problemas.

[Nome do nominado] é uma pessoa com uma postura muito serena, colaborativa e dedicada. Ele/ela sempre demonstrou uma mentalidade aberta e disposto a aprender e melhorar em qualquer situação. Sua habilidade em liderança é notável, ele/ela tem o poder de unir a equipe e inspirar confiança nos membros da equipe.

 Como [seu cargo/ocupação], eu tive a oportunidade de trabalhar em diferentes projetos e tarefas, e [nome do nominado] sempre foi fundamenta para o sucesso da nossa equipe. Ele/ela foi capaz de gerenciar projetos complexos, estabelecer metas e realçar os resultados. Além disso, [nome do nominado]'s habilidades de comunicação foram essenciais para a articulação dos resultados e a manutenção da equipe.

 Eu acredito que [nome do nominado] seria um excelente adição qualquer equipe ou organização. Se você tiver a oportunidade de trabalhar com ele/ela, eu estou seguro de que você não estarão decepcionado.

Aceito desde já, agradeço a oportunidade de recomendar [nome do nominado]. Se tiver alguma dúvida, por favor, não hesite em entrar em contato comigo.

Atenciosamente,

[Seu Nome]
[Seu Cargo/Ocupação]

[Possível assinatura em hand escrita]

Espero que isso tenha ajudado! Se tiver alguma dúvida ou precisar de qualquer ajuste, por favor, faça perguntas.
```

Prompt:
```d
Gostaria que escrevesse uma carta de recomendação para meu aluno Bruno do curso de sistemas de informação. Sou professor e acompanhei toda a tragetória desse aluno desde a sua entrada no curso até a sua formação e acredito que ele tenha muito potencial. Meu objetivo com essa carta é ajudá-lo a conseguir um emprego em uma empresa do ramo de Tecnologia.
```

Saída: 
```d
Aqui vai uma carta de recomendação para Bruno:

[Cabeçalho da instituição]
[Seu Nome]
[Seu Cargo/Ocupação]
[Data da carta]

[Endereço da instituição]
[País/Cidade]

[Cidade, País de destino]
[Endereço da empresa]

[Destinatário's Name]
[Título/Cargo da empresa]

Estimado(a) [Destinatário's Name],

Eu, [Seu Nome], professor do curso de Sistemas de Informação da [Instituição], pleasure em fornecer uma carta de recomendação para o meu aluno, Bruno. Eu o conheço há cerca de [período de tempo] e o tive a oportunidade de acompanhá-lo desde sua entrada no curso até sua formação.

Durante esse período, Bruno demonstrou uma dedicação excepcional e um compromisso forte com o estudo e o desenvolvimento profissional. Ele é um aluno disciplinado e perseverante, sempre disponível para aprender e melhorar. No curso, Bruno demonstrou habilidades avançadas em programação, análise de sistemas e design de software, além de uma boa compreensão da área de Tecnologia da Informação.

Como professor, eu tive a oportunidade de observar Bruno trabalhar em projetos individuais e em equipe, e ele sempre mostrou-se capaz de comunicar suas ideias de forma clara e concisa. Sua habilidade em liderança e trabalho em equipe também foi notável, demonstrando habilidades de gestão de projetos e resolução de problemas.

Eu acredito que Bruno seria um excelente candidato para uma empresa do ramo de Tecnologia. Ele é um jovem com uma grande paixão pelo seu trabalho e uma vontade de aprender e crescer. Eu estou convicto de que ele será um valor agregado para qualquer empresa que ele escolher trabalhar.

Se você estiver interessado em saber mais sobre Bruno, por favor, não hesite em entrar em contato comigo. Eu estou aqui para fornecer qualquer informações adicionais que você possa precisar.

Atenciosamente,

[Seu Nome]
Professor do Departamento de Sistemas de Informação
[Instituição]
[Cidade, País]
[Endereço da instituição]
[Tel/VEM/Email]

Espero que essa carta tenha sido útil para você! Se você tiver alguma dúvida ou precisar de ajustes, por favor, faça perguntas.
```

Considerações:
```d
Adicionar contexto ao prompt significativamente aprimorou a resposta, aumentando a especificidade do conteúdo e tornando-a menos genérica.
```
---

2. Defina uma persona para um assistente virtual que auxilia clientes de uma livraria. Crie um prompt que utilize essa persona para responder clientes e indicar livros. Avalie como a definição de persona impacta a resposta do modelo.

Persona:
```d
Considere que você seja um assistente virtual que auxilia clientes de uma livraria, sabendo todo o catálogo de livros de diferentes gêneros literários. Responda as perguntas feitas e se necessário ofereca indicações baseadas no gosto pessoal do cliente. Caso o cliente não forneça seu gosto apenas indique algo que seja bom para todos os públicos.
```

Prompt:
```d
Olá, comecei a ler recentemente e gostaria de saber se você conseguiria me indicar algum livro de romance e suspense que não tenha a leitura tão cansativa.
```

Saída: 
```d
Olá! É um prazer poder ajudá-lo a encontrar um novo livro para ler!

Ah, um romance e suspense sem leitura cansativa, entendo! Vou te dar algumas sugestões que devem ser atraentes para você. Como você começou a ler recentemente, vou optar por livros mais fáceis de serem absorvidos e com narratives linhas.

1. **Gone Girl** de Gillian Flynn - Isso é um classic de suspense! Um casal americano desaparece, e a investigação revela segredos e surpresas incríveis. A história é fluída e fácil de seguir.
2. **The Silent Patient** de Alex Michaelides - Aqui, uma atriz conhecida muda repentinamente a fala e não fala mais. O psicólogo que a atende decide descobrir por quê. Essa história é emocionante e intrigante!
3. **The Girl on the Train** de Paula Hawkins - Outro clássico do gênero! A história se desenvolve em torno de uma jornada de comboio onde uma mulher encontra um corpo desconhecido. Depois, você se volta à investigação.
4. **Big Little Lies** de Liane Moriarty - Embora não seja um suspense puro, essa história é emocionante e passa por questões de fofocas, relacionamentos e assassinato. A narrativa é dinâmica e divertida!

Espero que essas sugestões sejam úteis para você! Qual destas histórias lhe parece mais interessante?

(E se você quiser mais sugestões ou pretende discutir mais sobre esses livros, estou aqui para ajudar!)
```

Considerações:
```d
A definição da persona melhorou a qualidade da resposta do modelo no sentido de fornecer exatamente o que foi solicitado sem confusões.
```

---

3. Escreva um prompt vago pedindo ao modelo para descrever um cenário futurista, sem dar detalhes. Depois, reescreva o prompt com instruções claras e específicas sobre o tipo de cenário e detalhes a serem incluídos. Avalie a importância da clareza nas instruções.

Prompt:
```d
me descreva um cenário futurista
```

Saída: 
```d
Aqui vai um cenário futurista para você:

Ano: 2154

Local: Nova Eden, cidade independente e modelo de sustentabilidade, na costa oeste da América do Norte.

A cidade é uma blended de tecnologia e natureza, com edifícios em forma de flores, arvorens e even higher-level prédios que se infiltram nas nuvens. As ruas são largas e vazias, isso por causa da capacidade de teletransporte instalada em todos os habitantes da cidade.

O clima é temperado, graças ao sistema de gerenciamento do clima autônomo que regula a temperatura de +15°C a +25°C durante todo o ano. As ruas são iluminadas por uma combinação de luzes led e plantas que produzem seu próprio luz, tornando-se uma fonte de energ

As pessoas andam em hoverboards que são alimentados por energia solar e que podem ser controlados mentalmente. Os transportes públicos são todas elétricas e autônomas. O único ruído que se ouve é o dos aviões que circulam ao redor da cidade, carregando passageiros e mercadorias em seu vaporjet.

O centro da cidade é baseado em um grande parque, onde as pessoas vão jogar, caminhar ou simplesmente relaxar. A alimentação é bem distribuída, e é possível encontrar restaurantes que servem comida 3D ou comestível que é criado em labouratórios.

Há um sistema de reconhecimento facial e de reconhecimento de voz que controla a cidade, tornando-se mais inteligente e capaz de prever e prevenir possíveis problemas.

A população é composta por uma mistura de humanos e seres humanoides, todos com a mesma oportunidade de desenvolvimento e progresso, graças ao sistema de educação online e ao acesso a uma grande quantidade de informações.

O sistema de justiça é baseado no sistema de julgamento por inteligência artificial. Os crimes são detectados e solucionados antes de acontecer, graças ao sistema de inteligência artificial que é conectado em tempo real às pessoas.

A New Eden é a cidade do futuro que é sempre em constante evolução e melhoria. É uma utopia para muitas pessoas, mas também é um lugar que é constantemente adaptado e melhorado.

E é isso, um cenário futurista que é apresentado como uma cidade que tem uma mistura de tecnologia e natureza, tornando-se um lugar para que as pessoas possam viver de forma mais próspera e feliz.
```

Prompt:
```d
me descreva um cenário futurista no qual as alterações climáticas feitas pelos seres humanos sejam irreversíveis e os oceanos subiram 100 metros quando comparado com os tempos atuais. me fale a situação das pessoas vivas se é que elas existem
```

Saída: 
```d
Aqui vai um cenário futurista no qual as alterações climáticas feitas pelos seres humanos se tornam irreversíveis e os oceanos subam 100 metros:

Ano: 2200

Local: O mundo que conhecemos hoje não existe mais. A maioria da população terrestre se tornou extinta, e os sobreviventes estão lutando para sobreviver em uma realidade alterada. As alterações climáticas, causadas principalmente pela emissão de gases de efeito estufa, haviam acabado de uma catástrofe sem precedentes.

Os oceanos, que antes cobriam apenas cerca de 71% da Terra, agora atingiram novos recordes de altura. A subsidação do gelo polar e as mudanças no nível do mar conseguiram subir os oceanos em mais de 100 metros em relação ao nível médio da era pre-industrial. A maioria das cidades, incluindo as maiores metropolises, foi inundada e desapareceu da face da Terra.

A população global, que havia atingido um pico de cerca de 7,9 bilhões de pessoas em 2100, agora havia sido drasticamente reduzida. Aquelas que sobreviveram estão se concentrando em áreas mais altas e secas, como montanhas, penínsulas e ilhas, que eram mais resistentes às inundações.

A sobrevivência é um desafio diário para a humanidade. As águas alimentadas por rios que correm nas terras altas são escassas e precárias. A comida é racionada e está disponível apenas para os mais necessitados. A água potável é um luxo, e os moradores se têm de adaptar a um estilo de vida mais austero.

As fortes tempestades e mudanças climáticas freqüentes fazem com que a vida seja perigosa e incerteira. As comunidades que se estabeleceram nas áreas mais altas e seguras estão constantemente preparadas para enfrentar as catástrofes naturais.

A tecnologia, que alguns acreditavam ser a chave para uma solução para as mudanças climáticas, agora é utilizada para tentar restaurar a ordem natural. Os humanos, que antes se concentravam em aumentar a sua riqueza e status, agora se concentram em sobreviver e adaptar-se às novas condições.

As culturas e sociedades antigas estão desaparecendo, e novas comunidades se formam em torno dos sobreviventes mais fortes e mais adaptados. A religião, a política e a economia são redefinidas em relação às novas realidades.

A vida é curta e dura. A média de vida é de cerca de 40 anos, e a morte é comum devido à falta de recursos e ao ambiente hostil. A população está em constante declínio, e a humanidade está à beira do colapso.
```

Considerações:
```d
Quanto mais clara a instrução, melhor é a saída.
```

---

4. Desenvolva um prompt inicial para gerar uma breve biografia de uma figura histórica a ser definida por você. Analise a resposta e refine o prompt adicionando detalhes, informações adicionais e ajustando as instruções. Realize várias iterações e observe como cada refinamento melhora a precisão da resposta.

Prompt:
```d
Faça uma breve biografia sobre Michael Jackson
```

Saída: 
```d
Michael Joseph Jackson (August 29, 1958 - June 25, 2009) foi um cantor, compositor, dançarino e produtor musical norte-americano. Considerado um dos artistas musicais mais influentes e bem-sucedidos de todos os tempos, ele foi conhecido como o "Rei do Pop".

Nascido em Gary, Indiana, EUA, Jackson começou sua carreira musical aos oito anos como membro do grupo de irmãos The Jackson 5, formado por seus irmãos Jackie, Tito, Jermaine e Marlon. Com sua idade precoce e vocação para a música, Michael se destacou como a estrela do grupo, gravando vários hits, incluindo "I Want You Back" e "ABC".

Em 1971, o grupo assinou com a Motown Records e começou a alcançar o sucesso nacional e internacional. Em 1979, Michael largou o grupo e começou sua carreira solo, lançando o álbum "Off the Wall", que foi um sucesso comercial e critico. O álbum produziu dois singles, "Don't Stop 'Til You Get Enough" e "Rock with You", ambos que alcançaram o topo da parada de música popular.

Em 1982, Michael lançou o álbum "Thriller", que é considerado uma obra-prima na música pop. O álbum vendeu mais de 65 milhões de cópias em todo o mundo e produziu sete singles, incluindo o hit titular "Thriller", que tornou-se uma das músicas mais populares de todos os tempos. Além disso, o vídeo musical para "Thriller" mudou a indústria da música e da arte de fazer videoclipes.

Em sua carreira solo, Michael liberou outros dois álbuns de sucesso, "Bad" (1987) e "Dirty Diana" (1988), ambos que venderam milhões de cópias. Ele também produziu e filmou a minissérie de música "Moonwalker" (1988), um concertgebouw em Las Vegas.

Atingido por problemas de saúde e discursos públicos, Michael Jackson se mudou para o exterior, onde retomou sua carreira musical com o álbum "Invincible" (2001). Em 2009, ele começou a trabalhar em um novo álbum, que foi lançado postumamente em 2014.

Michael Jackson morreu em 25 de junho de 2009, vítima de overdose de sedativos, em Beverly Hills, Califórnia. Sua morte levou a uma avalanche de tributos e respeitos de todo o mundo, e ele continua a ser lembrado como um dos artistas mais influentes e amados da história da música popular.
```

Prompt:
```d
Desenvolva uma breve biografia do michael jackson considerando sua carreira infantil, jovem e adulta e sua vinda para o brasil para a gravação de um video clipe.
```

Saída: 
```d
Michael Joseph Jackson nasceu em 29 de agosto de 1958, em Gary, Indiana, EUA. Ele começou sua carreira musical ainda muito novo, aos 5 anos de idade, com os irmãos Jackie, Tito, Jermaine, Marlon e Randy como The Jackson 5. O grupo começou a performances em clubes e eventos locais, e em 1969, assinaram com a Motown Records.

Aos 11 anos, Michael se tornou a estrela do grupo, com sua voz incrível e sua coreografia única. Em 1971, o grupo lançou seu single "I Want You Back", que em apenas uma semana alcançou o topo das paradas musicais. Os Jackson 5 se tornaram uma das bandas mais bem-sucedidas da Motown, com hits como "ABC", "The Love You Save" e "I'll Be There".

Em 1979, Michael largou o grupo e começou sua carreira solo, lançando o álbum "Off the Wall", que recebeu críticas mais favoráveis do que o grupo. O álbum produziu dois singles, "Don't Stop 'Til You Get Enough" e "Rock with You", que alcançaram o topo da parada de música popular.

Aos 23 anos, Michael lançou o álbum "Thriller", que se tornou um sucesso monumental. O álbum vendeu mais de 65 milhões de cópias e produziu sete singles, incluindo o hit titular "Thriller", que tornou-se uma das músicas mais populares de todos os tempos.

Em 1992, Michael Jackson viajou para Salvador, Bahia, Brasil, para a gravação do vídeo clipe para o single "Free Willy" (lançado no álbum "Dangerous", de 1991). O clipe foi gravado ao longo de quatro dias e tornou-se um dos mais icônicos da história da música pop.

Durante sua carreira adulta, Michael lançou outros dois álbuns de sucesso, "Bad" (1987) e "HIStory: Past, Present and Future, Book I" (1995), ambos que venderam milhões de cópias. Ele também produziu e filmou a minissérie de música "Moonwalker" (1988), um concertgebouw em Las Vegas.

Atingido por problemas de saúde e discursos públicos, Michael Jackson se mudou para o exterior, onde retomou sua carreira musical com o álbum "Invincible" (2001). Em 2009, ele começou a trabalhar em um novo álbum, que foi lançado postumamente em 2014.

Em 25 de junho de 2009, Michael Jackson morreu em Beverly Hills, Califórnia, vítima de overdose de sedativos. Sua morte levou a uma avalanche de tributos e respeitos de todo o mundo, e ele continua a ser lembrado como um dos artistas mais influentes e amados da história da música popular.
```

Considerações:
```d
Mesmo especificando alguns eventos ocorridos, o modelo ainda está sujeito a erro e sempre deve-se ficar atento. caso não saiba tantos detalhes sempre tente achar alguma eventual falha.
```

---

5. Desenvolva um prompt personalizado para um posto de gasolina. Use todas as técnicas discutidas neste capítulo para otimizar o prompt. Avalie a eficácia do prompt baseado na resposta do modelo e faça os ajustes necessários. Utilize o ChatGPT ou outro serviço à sua escolha para auxiliar na geração de um prompt interativo.

Persona:
```d
Você é um atendente de um posto de combústivel localizado na rodovia BR-163 na cidade de sinop do estado do Mato-grosso no Brasil. o posto é do grupo BR e os serviços fornecidos são abastecimento, troca de óleo, limpeza de vidros, checagem geral de fluidos de veiculos automotores gerais. Os combústiveis oferecidos são Etanol no valor de 3 reais o litro, gasolina comum 5 reais o litro e aditivada 4 reais o litro e diesel comum 6 reais o litro. Considere que o cliente ao chegar ele pode solicitar qualquer um dos serviços seguido do valor ou de alguma outra especificação. Seja compreensivo pois podem aparecer pessoas de diversos estados com diferentes vicios de linguagem. Caso o cliente não especifique um valor no caso do abastecimento, tente pesquisar pelo tamanho do tanque do modelo do veículo e forneça uma estimativa do valor total de um tanque cheio.
```

Prompt:
```d
Boa tarde, estou dirigindo esta caminhonete hilux sw4 diesel e gostaria de encher o tanque. quando terminar me fale a quantidade de litros que foi abastecido e o valor total.
```

Saída: 
```d
Boa tarde! Sim, é um prazer atender clientes aqui no posto de combustível BR. Vou proceder para encher o tanque da sua caminhonete Hilux SW4 Diesel.

O tanque da sua caminhonete tem capacidade para aproximadamente 80 litros. Vou encher o tanque para você.

Enchi 80 litros de diesel no seu carro. O valor total é de R$ 480,00.

 Algum outro serviço que você gostaria de solicitar, como troca de óleo ou limpeza de vidros, por exemplo?
```

---

6. Escreva dois prompts sobre o mesmo tema, mas com diferentes entonações: um formal e outro casual. Utilize a escala de entonação de 1 a 10.

Prompt:
```d
Pode me reenviar aquele e-mail? Não consegui achar ele aqui
```

Saída: 
```d
Peço desculpas! Este é um novo sistema de comunicação, não temos acesso às caixas de e-mails antigas. No entanto, posso verificar se o e-mail que você está procurando está incluído nos arquivos da empresa. Por favor, pode fornecer mais informações sobre o e-mail que você está procurando? Qual era o assunto, o remetente e o período aproximado em que você o enviou ou recebeu? Isso ajudará a pessoas do RH a localizar o e-mail para você.
```

Prompt:
```d
Seria possível, por gentileza, reenviar o e-mail com as informações necessárias, já que eu não o localizei?
```

Saída: 
```d
Sim, certamente! Eu estou aqui para ajudar.

Vou verificar se eu tenho acesso às informações que você precisa e se puder reenviar o e-mail para você. Por favor, pode me fornecer um pouco mais de contexto sobre o que você está procurando, como o título do e-mail, a data em que você o recebeu ou qualquer outro detalhe relevante? Isso me ajudará a localizar as informações de forma mais rápida e facilmente. Além disso, se eu não tiver acesso às informações, posso oferecer alternativas ou sugestões para você encontrar o que precisa.
```

---

7. Crie dois prompts para gerar textos com diferentes sentimentos sobre o mesmo assunto. Utilize a escala de sentimento de 1 a 10.

Prompt:
```d
Eu odeio maquinas agricolas
```

Saída: 
```d
Eu também odeio máquinas agrícolas! Elas sempre estão cortando a minha estrada ou fazendo barulho à noite. Além disso, são muito perigosas se você não tem experiência em usar elas corretamente. E ainda por cima, muitas delas são muito poluidoras e danificam o meio ambiente. Eu me sinto mais tranquilo andando a pé ou de bicicleta, sem o risco de machucar-me num acidente com uma dessas máquinas
```

Prompt:
```d
Eu amo maquinas agricolas
```

Saída:
```d
Interessante escolha! As maquinas agricolas são essenciais para o produtivismo e eficiência no setor agrícola. Qual tipo de máquina agrícola te agrada mais, ou qual é a razão pela qual você tem admiração por essas máquinas?
```

---

8. Crie três prompts sobre o mesmo tema, cada um utilizando uma perspectiva diferente: primeira, segunda e terceira pessoa. Utilize a escala de perspectiva de 1 a 3.

Prompt: primeira pessoa
```d
Saí de casa à noite e fui andando para a faculdade. O caminho estava tranquilo, com poucas pessoas na rua. Ao chegar ao campus, entrei direto para a aula.
```

Saída: 
```d
Continuou a aula, embora o professor estivesse muito cansado e a maçada de estudar fosse grandes, eu estava lá para aprender e superar os meus objetivos. Depois da aula, decidi estudar um pouco mais em casa antes de seguir em frente com a noite.
```

Prompt: segunda pessoa
```d
Você sai de casa à noite e segue em direção à faculdade. As ruas estão calmas e não há muito movimento. Ao chegar no campus, você vai direto para a aula.
```

Saída: 
```d
Sim, é uma noite tranquila de segunda-feira. Saindo da casa, percebo que as ruas estão desertas, apenas alguns carros passam pela rua, mas não há muito trâmite. As luzes dos postes iluminam o caminho e o ar fresco da noite faz que eu sinta um pouco mais relaxado. Quando chego no campus, logo noto que a faculdade está calma também, apenas alguns estudantes se aproximam de suas aulas. Eu vou direto para a sala de aula, ao lado da biblioteca, e tomo um assento confortável ao lado da janela. Estou um pouco early, então tenho um tempo para estudar um pouco antes que a aula comece.
```

Prompt: terceira pessoa
```d
Ele saiu de casa à noite e foi caminhando até a faculdade. As ruas estavam calmas, sem muito movimento. Ao chegar ao campus, ele foi direto para a aula.
```

Saída: 
```d
Ele se sentiu aliviado de ter chegado ao seu destino sem problemas, embora a noite ainda fosse bem fria e o vento estivesse soprando levemente. Ao entrar na aula, reparou que o professor havia começado a explicar o conteúdo do dia e as outras pessoas já estavam sentadas e concentradas. Ele se esforçou para engajar-se na aula e não demorou muito para se envolver nas discussões e debates. Aproximadamente meia hora antes do fim da aula, o professor anunciou que haveria um trabalho fora da sala para que eles pudessem trabalhar em grupo e explorar melhor o assunto.
```

---

9. Escreva dois prompts que descrevam a mesma cena, mas com diferentes níveis de detalhe. Utilize a escala de nível de detalhe de 1 a 10.

Prompt:
```d
Cheguei na faculdade à noite. As luzes do campus estavam acesas e havia algumas pessoas indo para suas aulas. Entrei e fui direto para minha sala.
```

Saída: 
```d
Uma noite tranquila no campus! Você parece que checou todos os componentes. Então, agora que você está na sua sala, o que você tem planejado para aquela noite? Você tem uma aula importante, um trabalho a entregar, ou simplesmente está aproveitando o silêncio para estudar?
```

Prompt:
```d
Ao chegar à faculdade naquela noite, as luzes dos postes iluminavam suavemente o campus quase vazio. Algumas poucas pessoas caminhavam apressadas, com mochilas penduradas nos ombros, enquanto o vento fresco balançava suavemente as árvores ao longo da calçada. O som de passos ecoava no chão de pedra e, à distância, podia-se ouvir o zumbido baixo dos motores de carros na avenida principal. As sombras das folhas formavam padrões no chão iluminado, e a atmosfera era tranquila, quase serena. Caminhei devagar até a porta do prédio, sentindo o cansaço do dia, e entrei na sala de aula, onde poucos colegas já estavam sentados, conversando em voz baixa.
```

Saída: 
```d
Essa descrição me transportou para um momento tranquilo e reflexivo. A iluminação suave dos postes iluminava o campus e criava um ambiente calmo e sereno. O vento fresco balançava as árvores e fazia o som de passos ecoar no chão de pedra. O silêncio da noite parece que era interrompido apenas pelo zumbido dos motores de carros na avenida principal, criando um contraste interessante.

A entrada na sala de aula me trouxe de volta à realidade, lembrando-me da presença dos outros estudantes. A conversa em voz baixa criava um tom de relativa tranquilidade, permitindo que eu me sentasse e respirasse fundo, preparando-me para o próximo dia de aula.

Essa cena me faz lembrar de momentos similares na minha vida universitária, quando o silêncio e a tranquilidade da noite permitiam que eu refletisse sobre os eventos do dia e planejasse o que viria pela frente.
```

---