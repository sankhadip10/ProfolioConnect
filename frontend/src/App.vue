<template>
  <div id="app">
    //<img alt="Vue logo" src="./assets/logo.png">
    //<HelloWorld msg="Welcome to Your Vue.js App"/>
    <LoginComponent/> <!-- This is where LoginComponent will appear -->
  </div>
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'; // If using HelloWorld
import LoginComponent from './components/LoginComponent.vue'; // Import LoginComponent

export default {
  name: 'App',
  components: {
    //HelloWorld,       // Register HelloWorld if it's being used
    LoginComponent    // Register LoginComponent
  }
};
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
