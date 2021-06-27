<template>
  <div>
    <v-container>
      <SalesAndRent />
      <Services2 />
      <About />
    </v-container>
</template>

<script>
import SalesAndRent from "@/components/home/SalesAndRent.vue"
import Services2 from "@/components/home/Services2.vue"
import About from "@/components/home/About.vue"


export default {
  name: 'Home',
  components: {
    SalesAndRent,
    Services2,
    About,
  },
  data() {
    return {
    }
  },
}

</script>
