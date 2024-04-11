<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <header>
    <!-- <img class="logo" src="./assets/logo.svg" width="200"> -->
    <div class="header-block">
      <div id="label">ВСЕРОССИЙСКАЯ ЯРМАРКА ТРУДОУСТРОЙСТВА <span id="year">2024</span></div>
      <div class="registration-block">
        <div id="registration-label">Мурманская область</div>
        <div id="registration-label">Заявка на регистрацию</div>
      </div>
    </div>
  </header>

  <div class="logos">
    <img class="logo-img" width="70px" src="./assets/img/icon-projects.png">
    <img class="logo-img" width="70px"src="./assets/img/icon-mintrud.png">
    <img class="logo-img" width="70px" src="./assets/img/icon-rostrud.png">
    <img class="logo-img" width="70px" src="./assets/img/icon-prr.png">
  </div>


  <footer>
    <div class="footer-punct">© Федеральная служба по труду и занятости — rostrud.ru.</div>
    <div class="footer-punct">trudvsem.ru </div>
    <div class="footer-punct">murman-zan.ru</div>
  </footer>

  <RouterView />
</template>

<style scoped>
header{
  background-color: var(--main-dark-blue-color);
}

#label{
  color: white;
  font-weight: bold;
  font-size: 20px;
}

#year{
  color: var(--main-red-color)
}

#registration-label{
  color: white;
}

.registration-block{
  margin-top: 20px;
}


.header-block{
  margin-left: 20px;
  margin-right: 20px;
  padding-top: 20px;
  padding-bottom: 20px;
  text-align: center;
}

footer{
  background-color: var(--main-dark-blue-color);
   position: fixed;
   right: 0;
   bottom: 0;
   text-align: center; 
   width: 100%;   
   padding-top: 20px;
   padding-bottom: 20px;
   font-size: 14px;
  color: #fafaff;  
}

.footer-punct{
  margin-top: 5px;
  margin-bottom: 5px;
}

.logos{
  margin-top: 15px;
  text-align: center;
}

.logo-img{
  margin-left: 5px;
  margin-right: 5px;
}
</style>
