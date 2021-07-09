<template>
  <div>
    <v-spacer> </v-spacer>
    <v-footer
      padless
    >
      <v-card
        flat
        tile
        class="text-center"
        width="100%"
        color="#846D34"
      >
        <v-card-text>
          <v-btn
            v-for="icon in icons"
            :key="icon"
            class="mx-4 white--text"
            :href="links[ icon ]"
            target="_blank"
            icon
          >
            <v-icon size="24px">
              {{ icon }}
            </v-icon>
          </v-btn>
        </v-card-text>

        <v-container>
          <v-row>
            <v-col>

              <v-avatar size="80">
                <img
                  src="https://cdn.vuetifyjs.com/images/john.jpg"
                  alt="John"
                >
              </v-avatar>
              <v-spacer></v-spacer>
              <v-list-item-content>
                <v-list-item-title class="text-h6 mb-1">
                  Valentin Vidalled
                </v-list-item-title>
                <v-list-item-subtitle>Martillero publico</v-list-item-subtitle>
                <v-list-item-subtitle>Matricula nro: 123456</v-list-item-subtitle>
              </v-list-item-content>
            </v-col>
             <v-col>
               <div class="d-flex flex-column justify-space-between align-center">

                 <v-img
                 src="@/assets/img/logo/fondo_tranparente_recortado.png"
                 max-height="170"
                 max-width="170"
                 ></v-img>
               </div>
               <v-divider></v-divider>
               <v-spacer></v-spacer>
               <strong>CONTACTO</strong>
               <v-spacer></v-spacer>
               Jose Gabino Blanco 1527 esq. Batalla de Cepeda
               <v-spacer></v-spacer>
               (351) 3651121
               (351) 6533887
               <v-spacer></v-spacer>
               inmo@test.com
             </v-col>
            <v-col>
              <v-avatar size="80">
                <img
                  src="https://cdn.vuetifyjs.com/images/john.jpg"
                  alt="John"
                >
              </v-avatar>
              <v-spacer></v-spacer>
              <v-list-item-content>
                <v-list-item-title class="text-h6 mb-1">
                  Francisco Camara
                </v-list-item-title>
                <v-list-item-subtitle>Martillero publico</v-list-item-subtitle>
                <v-list-item-subtitle>Matricula nro: 123456</v-list-item-subtitle>
              </v-list-item-content>
            </v-col>
          </v-row>
        </v-container>

        <v-divider></v-divider>

        <v-card-text class="white--text">
          Copyright 2021
        </v-card-text>
      </v-card>
    </v-footer>
    </div>
</template>

<script>
  export default {
    data: () => ({
      icons: [
        'mdi-facebook',
        'mdi-instagram',
      ],
      links: {
        'mdi-facebook':'https://www.facebook.com/inmobiliariavidalledcamara',
        'mdi-instagram':'https://www.instagram.com/vidalledcamara/',
      },
    }),
  }
</script>
