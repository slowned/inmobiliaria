<template>
  <div id="app">
    <div id="nav">
      <router-link :to="{ name: 'Properties' }">Alquileres</router-link> |
      <router-link to="#">Ventas</router-link> |
      <router-link to="#">Nosotros</router-link> |
      <router-link to="#">Contacto</router-link>
    </div>
    <router-view/>
    <div>
      <Footer/>
    </div>
  </div>
</template>

<script>
import Footer from '@/components/Footer.vue';

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
