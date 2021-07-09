<template>
  <v-container fluid>
    <v-row>
      <v-col>
        <v-card
        width="100%"
        height="auto"
        color="#BAA460"
        elevation="8"
        >
        <v-card-title class="text-h6">
          Una propuesta de vanguardia para el rubro inmobiliario
        </v-card-title>
        <v-card-text>
            Nuestros valores transmiten responsabilidad, seriedad y confianza, como así también entusiasmo y juventud.
            Creemos en el uso de la tecnología y métodos digitales, para garantizar así un trabajo especializado y de la misma manera contribuir con el medio ambiente.
            Nuestro objetivo es crecer junto a los clientes que nos elijan, generar lazos de confianza y darle una buena imagen a la actividad.
            <v-divider></v-divider>
        </v-card-text>

        <template>
          <v-row>
            <v-col cols="12" sm="4">
              <v-img
              :src="`https://picsum.photos/500/300?image=35`"
              :lazy-src="`https://picsum.photos/10/6?image=15`"
              max-height="200"
              aspect-ratio="1"
              class="grey lighten-2"
              ></v-img>
            </v-col>
            <v-col cols="12" sm="4">
              <video-background
                :src="require(`@/assets/presentacion.mp4`)"
                style=" height: 200px;"
              >
                <h1 style="color: white;"></h1>
              </video-background>
            </v-col>
            <v-col cols="12" sm="4">
              <v-img
              :src="`https://picsum.photos/500/300?image=59`"
              :lazy-src="`https://picsum.photos/10/6?image=11`"
              max-height="200"
              aspect-ratio="1"
              class="grey lighten-2"
              ></v-img>
            </v-col>
          </v-row>
        </template>
      </v-card>
    </v-col>
  </v-row>
</v-container>
</template>


<script>
import VideoBackground from 'vue-responsive-video-background-player'
export default {
  name: "",
  components: {
    VideoBackground
  },
  data: () => ({

  })
}
</script>
<style lang="scss" scoped>
</style>
