<template>
    <v-container>
      <!-- servicios -->
      <Service />
      <!-- imagenes chetas -->
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
          <v-img
            :src="`https://picsum.photos/500/300?image=30`"
            :lazy-src="`https://picsum.photos/10/6?image=35`"
            aspect-ratio="1"
            class="grey lighten-2"
          ></v-img>
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

      <!-- nosotros -->
      <v-row>
        <v-col>
          <v-card
            color="#385F73"
            dark
          >
            <v-card-title class="text-h5">
              Quienes somos titulo
            </v-card-title>

            <v-card-subtitle>Listen to your favorite artists and albums whenever and wherever, online and offline.</v-card-subtitle>
          </v-card>
        </v-col>
      </v-row>
    </v-container>

</template>

<script>
import Service from "@/components/home/Services.vue"

export default {
  name: 'Home',
  components: {
    Service,
  },
  data() {
    return {
      card: "sara",
    }
  },
}

</script>
