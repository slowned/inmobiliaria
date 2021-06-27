<template>
  <v-app>

    <Header />

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
import Header from "@/components/Header.vue"

export default {
  name: 'App',
  components: {
    Footer,
    Header,
  },
  data() {
    return {
    }
  },
}
</script>

<style>
</style>
