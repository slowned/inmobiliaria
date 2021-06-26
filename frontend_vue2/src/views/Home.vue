<template>
    <v-container>
      <!-- servicios -->
      <SalesAndRent />
      <Services2 />
      <About />
      <!-- imagenes chetas -->
      <v-container fluid>
        <v-row>
          <v-col>
            <v-img
              :src="`https://picsum.photos/500/300?image=20`"
              :lazy-src="`https://picsum.photos/10/6?image=25`"
              aspect-ratio="1"
              class="grey lighten-2"
            ></v-img>
          </v-col>

          <v-col>
            <video-background
              :src="require(`@/assets/presentacion.mp4`)"
              style="max-height: 360px; height: 100vh;"
            >
              <h1 style="color: white;">Hello welcome!</h1>
            </video-background>
          </v-col>

          <v-col>
            <v-img
              :src="`https://picsum.photos/500/300?image=10`"
              :lazy-src="`https://picsum.photos/10/6?image=15`"
              aspect-ratio="1"
              class="grey lighten-2"
            ></v-img>
          </v-col>
        </v-row>
      </v-container>
    </v-container>

</template>

<script>
import SalesAndRent from "@/components/home/SalesAndRent.vue"
import Services2 from "@/components/home/Services2.vue"
import About from "@/components/home/About.vue"
import VideoBackground from 'vue-responsive-video-background-player'


export default {
  name: 'Home',
  components: {
    SalesAndRent,
    Services2,
    About,
    VideoBackground

  },
  data() {
    return {
    }
  },
}

</script>
