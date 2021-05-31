<template>
  <div class="block galleryBlock">
    <v-container>
      <v-row>
        <v-col v-for="item in items" :key="item.id" class="d-flex child-flex" cols="6" sm="4">
          <v-hover v-slot="{ hover }">
              <v-card
                flat tile class="d-flex"
                :class="{ 'on-hover': hover }"
              >
              <v-img :src="item.src" aspect-ratio="1" class="grey lighten-2">
                <template v-slot:placeholder>
                  <v-row class="fill-height ma-0" align="center" justify="center">
                    <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
                  </v-row>
                </template>
                <div class="center">
                  <h3 class="cardTitle">{{ item.title }}</h3>
                </div>
              </v-img>
            </v-card>
          </v-hover>
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
      dialog: false,
      items: [
        {
          id: 1,
          title: "Tasaciones",
          src: 'https://la.network/wp-content/uploads/2019/09/mario-home.jpg',
          description: "Una buena tasación requiere de la correcta aplicación de las distintas técnicas que forman la actividad de tasar una propiedad, por eso queremos informarte que contamos con la formación profesional y académica necesaria para justipreciar un inmueble.  Realiza tu consulta sin cargo para mayor información, nosotros te ayudamos.",
        },
        {
          id: 2,
          title: "Loteos",
          src: 'https://la.network/wp-content/uploads/2019/09/mario-home.jpg',
          description: "Contamos con experiencia dentro de la inmobiliaria para el manejo y administración de venta de tierras a gran escala, con distintas formas de aplicación según varíe el método de pago.  Tenemos a disposición los profesionales necesarios para llevar a cabo el trabajo que implica el desarrollo de un loteo.  Realiza tu consulta sin cargo para mayor información, nosotros te ayudamos.",
        },
        {
          id: 3,
          title: "Consorcios",
          src: 'https://la.network/wp-content/uploads/2019/09/mario-home.jpg',
          description: "Nuestra administración de consorcios cuenta con el soporte en software para el pago de las expensas y gastos que la figura del consorcio demande, como así también una atención especializada para toda situación que sea necesaria la intervención de la administración.  Realiza tu consulta sin cargo para mayor información, nosotros te ayudamos.",
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
    font-weight: bold;
    font-family: cursive;
}
.center {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.v-card {
  transition: opacity .4s ease-in-out;
}

.v-card:not(.on-hover) {
  opacity: 0.6;
 }
</style>
