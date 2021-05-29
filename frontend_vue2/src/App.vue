<template>
  <v-app>
    <v-app-bar app
      src="@/assets/logo.png"
      color="grey lighten-2"
    >
      <v-toolbar-title>
        <img class="mr-3" src="@/assets/logo.png" height="50"/>
      </v-toolbar-title>

      <v-spacer></v-spacer>

      <div id="nav">
        <router-link :to="{ name: 'Home' }">INICIO</router-link> |
        <router-link :to="{ name: 'Properties' }">Alquileres</router-link> |
        <router-link to="#">Ventas</router-link> |
        <router-link to="#">Nosotros</router-link> |
        <router-link to="#">Contacto</router-link>
      </div>

    </v-app-bar>
    <v-main>

    <!-- Provides the application the proper gutter -->
    <v-container fluid>

      <!-- If using vue-router -->
      <router-view></router-view>
      
      <Footer />
    </v-container>


    </v-main>


  </v-app>
</template>

<script>

import Footer from "@/components/Footer.vue"

export default {
  name: 'App',
  components: {
    Footer,
  },
  data() {
    return {
    }
  },
}
</script>

<style>
</style>
