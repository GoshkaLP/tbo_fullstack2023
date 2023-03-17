<template>
  <div>
    <div class="page">
      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Roboto&display=swap" rel="stylesheet">
      <header class="header">
        <!--        <video src="./images/planet-earth.webm" class="header__main-illustration" autoplay loop></video>-->
        <img src="../assets/planet-earth.png" alt="Планета Земля" class="header__main-illustration">
        <img src="../assets/arrow.png" alt="123" class="header__arrow-illustration">
        <img src="../assets/interactive-map.png" alt="Надпись: 'интерактивная карта'" class="header__text-illustration">
        <h1 class="header__title">спортивных объектов</h1>
      </header>

      <main class="content">
        <section class="about">
          <h2 class="about__title">Что это за сервис?</h2>
          <p class="about__text">
            Перед вами – карта, которая объединяет в себе
            <a href="https://data.gov.ru/opendata/7703771271-sportobjects" class="about__link">данные</a>
            по всем спортивным объектам&nbsp;в&nbsp;России. Узнайте, как год за годом изменялась
            спортивная инфраструктура страны, какие субъекты РФ могут похвастаться самым лучшим
            спортивным оснащением, и множество других не менее интересных фактов. Вперед!
          </p>
        </section>

        <section class="features">
          <div class="features__title-box">
            <h2 class="features__title">
              возможн<span class="features__title_accent_purple">ос</span>ти--<span class="features__title_accent_green">возможности</span>--возможности
            </h2>
          </div>
          <ul class="features__list">
            <li>
              <article class="feature">
                <div class="feature__first-column">
                  <img src="../assets/feature-image-1.png" alt="" class="feature__illustration">
                </div>
                <div class="feature__second-column">
                  <p class="feature__count">1</p>
                  <h3 class="feature__title">Аналитика объектов</h3>
                  <p class="feature__text">
                    Каждый объект – точка на карте. При уменьшении масштаба объекты
                    объединяются в группы по местоположению. При нажатии на объект
                    можно получить подробный отчет о нем: общую информацию, детализацию
                    финансирования и контакты.
                  </p>
                </div>
              </article>
            </li>
            <li>
              <article class="feature">
                <div class="feature__first-column">
                  <img src="../assets/feature-image-2.png" alt="" class="feature__illustration">
                </div>
                <div class="feature__second-column">
                  <p class="feature__count">2</p>
                  <h3 class="feature__title">Аналитика регионов</h3>
                  <p class="feature__text">
                    На интерактивной карте вы можете изучить распределение спортивных
                    объектов по регионам. Чем темнее регион – тем больше объектов,
                    чем светлее – тем меньше. При помощи фильтра можно оставить только
                    интересующие вас субъекты РФ, чтобы работать с ними.
                  </p>
                </div>
              </article>
            </li>
            <li>
              <article class="feature">
                <div class="feature__first-column">
                  <img src="../assets/feature-image-3.png" alt="" class="feature__illustration">
                </div>
                <div class="feature__second-column">
                  <p class="feature__count">3</p>
                  <h3 class="feature__title">Временная линия</h3>
                  <p class="feature__text">
                    Двигайте ползунок, чтобы увидеть, где с течением времени строились
                    новые спортивные объекты. Цвет полигонов зависит от типа
                    построенных спортивных объектов.
                  </p>
                </div>
              </article>
            </li>
            <li>
              <article class="feature">
                <div class="feature__first-column">
                  <img src="../assets/feature-image-4.png" alt="" class="feature__illustration">
                </div>
                <div class="feature__second-column">
                  <p class="feature__count">4</p>
                  <h3 class="feature__title">Итоговая сводка</h3>
                  <p class="feature__text">
                    В отдельной вкладке собраны графики и диаграммы, которые
                    позволяют детально изучить информацию о спортивных
                    объектах: в динамике и в обобщенном виде.
                  </p>
                </div>
              </article>
            </li>
          </ul>
          <div class="features__title-box">
            <p class="features__title">
              возможност<span class="features__title_accent_green">и-</span>-возможн<span class="features__title_accent_purple">ос</span>ти--возможности
            </p>
          </div>
        </section>
      </main>

      <footer class="footer">
        <p class="footer__description">
          Чтобы вернуться к подсказкам позднее, нажмите “?” в правом верхнем углу экрана.
        </p>
      </footer>
    </div>
  </div>
</template>

<script>
export default {
  name: "HelpComponent"
}
</script>

<style scoped>
@keyframes rotate {
  from {transform: rotate(238deg);}
  to {transform: rotate(598deg);}
}

.page {
  margin: 0 auto;
  font-family: 'Roboto', sans-serif;
  font-weight: 400;
  background: radial-gradient(133.5% 159.28% at 0% 31.14%,
  rgba(0, 0, 0, 0.2) 0%, rgba(0, 0, 0, 0.2) 0%,
  rgba(0, 0, 0, 0.2) 0%, rgba(0, 0, 0, 0.2) 0.01%,
  rgba(0, 0, 0, 0) 100%);
  max-width: 1024px;
}

/* Стили шапки. */

.header {
  height: 474px;
  padding-bottom: 6px;
  position: relative;
  display: flex;
  align-items: center;
  gap: 170px;
}

.header__main-illustration {
  height: 300px;
  margin: -55px;
  object-fit: cover;
  position: relative;
  z-index: 2;
}

.header__arrow-illustration {
  width: 350px;
  position: absolute;
  top: 0;
  left: 70px;
}

.header__text-illustration {
  max-width: 410px;
  position: absolute;
  top: 35px;
  left: -110px;
  animation: rotate 10s infinite linear;
}

.header__title {
  margin: 0;
  padding: 0;
  max-width: 400px;
  color: #3B1B64;
  font-family: 'Press Start 2P', cursive;
  font-size: 40px;
  line-height: 44px;
}

/* Стили интро. */

.about {
  margin-top: 50px;
  margin-left: 60px;
  max-width: 690px;
}

.about__title {
  margin: 0;
  padding: 0;
  font-family: 'Press Start 2P', cursive;
  font-size: 20px;
  line-height: 22px;
}

.about__text {
  margin: 20px 0 0;
  padding: 0;
  font-size: 16px;
  line-height: 26px;
}

.about__link {
  color: #3B1B64;
  font-weight: bold;
  text-decoration: none;
  border-bottom: #3B1B64 solid 2px;
  transition: opacity 0.5s;
}

.about__link:hover {
  opacity: 0.7;
}

/* Стили возможностей. */

.features {
  background-image: url('@/assets/features-background.png');
  background-size: min(100vw, 1024px);
  background-repeat: no-repeat;
  margin-top: 60px;
  min-height: 1762px;
}

.features__title-box {
  width: 100%;
  height: 98px;
  overflow: hidden;
  position: relative;
}

.features__title {
  margin: 54px 0 0;
  padding: 0;
  width: 1480px;
  position: absolute;
  top: 0;
  left: -228px;
  font-family: 'Press Start 2P', cursive;
  font-size: 40px;
  line-height: 44px;
}

.features__title_accent_purple {
  color: #3B1B64;
}

.features__title_accent_green {
  color: #71F9D0;
}

.features__list {
  margin: 60px 0 0;
  padding: 0;
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 52px;
}

.feature {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 30px;
}

.feature__first-column {
  max-width: 580px;
}

.feature__illustration {
  max-width: 580px;
  aspect-ratio: 290/159;
  border: 2px solid black;
  box-sizing: border-box;
  object-fit: cover;
}

.feature__second-column {
  display: flex;
  flex-wrap: wrap;
  row-gap: 14px;
  column-gap: 10px;
  max-width: 294px;
}

.feature__count {
  margin: 0;
  padding: 0;
  color: #71F9D0;
  font-family: 'Press Start 2P', cursive;
  font-size: 48px;
  line-height: 48px;
}

.feature__title {
  margin: 0;
  padding: 0;
  max-width: 233px;
  font-family: 'Press Start 2P', cursive;
  font-size: 20px;
  line-height: 22px;
}

.feature__text {
  margin: 0;
  padding: 0;
  font-size: 16px;
  line-height: 26px;
}

/* Стили подвала. */

.footer {
  margin: 60px 0 0;
  padding-bottom: 30px;
}

.footer__description {
  margin: 0;
  padding: 0;
  text-align: center;
  font-size: 16px;
  line-height: 26px;
}

</style>