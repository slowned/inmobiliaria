<template>
  <div class="block galleryBlock">
    <v-container fluid>
      <v-row>
        <v-col v-for="item in items" :key="item.id" class="d-flex child-flex" cols="12" sm="4">
            <v-dialog
              transition="dialog-bottom-transition"
              max-width="600"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-card
                  flat tile class="d-flex"
                  elevation="8"
                  v-bind="attrs"
                  v-on="on"
                >
                  <v-img :src="item.src" aspect-ratio="1" class="grey lighten-2">
                    <template v-slot:placeholder>
                      <v-row class="fill-height ma-0" align="center" justify="center">
                        <v-progress-circular indeterminate color="#BAA460"></v-progress-circular>
                      </v-row>
                    </template>
                    <div class="center">
                      <h3 class="cardTitle">{{ item.title }}</h3>
                    </div>
                  </v-img>
                </v-card>
              </template>
              <template v-slot:default="dialog">
                <v-card>
                  <v-toolbar
                    color="#846D34"
                    dark
                  >{{ item.title }}</v-toolbar>
                  <v-card-text>
                    <div class="pa-5">{{ item.message }}</div>
                  </v-card-text>
                  <v-card-actions class="justify-end">
                    <v-btn
                      text
                      @click="dialog.value = false"
                    >Cerrar</v-btn>
                  </v-card-actions>
                </v-card>
              </template>
            </v-dialog>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "Services2",
  data() {
    return {
      items: [
        {
          id: 1,
          title: "Tasaciones",
          message: "Una buena tasación requiere de la correcta aplicación de las distintas técnicas que forman la actividad de tasar una propiedad, por eso queremos informarte que contamos con la formación profesional y académica necesaria para justipreciar un inmueble. Realiza tu consulta sin cargo para mayor información, nosotros te ayudamos.",
          src: 'https://la.network/wp-content/uploads/2019/09/mario-home.jpg'
        },
        {
          id: 2,
          title: "Loteos",
          message: "Contamos con experiencia dentro de la inmobiliaria para el manejo y administración de venta de tierras a gran escala, con distintas formas de aplicación según varíe el método de pago. Tenemos a disposición los profesionales necesarios para llevar a cabo el trabajo que implica el desarrollo de un loteo. Realiza tu consulta sin cargo para mayor información, nosotros te ayudamos.",
          src: 'https://la.network/wp-content/uploads/2019/09/mario-home.jpg'
        },
        {
          id: 3,
          title: "Consorcios",
          message: "Nuestra administración de consorcios cuenta con el soporte en software para el pago de las expensas y gastos que la figura del consorcio demande, como así también una atención especializada para toda situación que sea necesaria la intervención de la administración.  Realiza tu consulta sin cargo para mayor información, nosotros te ayudamos.",
          src: 'https://la.network/wp-content/uploads/2019/09/mario-home.jpg'
        }
      ],
      transparent: 'rgba(255, 255, 255, 0)',
    };
  }
};
</script>

<style scoped>
.cardTitle {
    text-align: center;
    font-size: 35px;
    font-family: 'Big Shoulders Stencil Display';
}
.center {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>
