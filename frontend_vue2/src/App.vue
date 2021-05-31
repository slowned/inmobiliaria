<template>
  <v-app>
    <v-app-bar app
      color="grey darken-4"
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
      <!-- If using vue-router -->
      <router-view></router-view>
    </v-main>
    <Footer />
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
