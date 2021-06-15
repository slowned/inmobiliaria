<template>
    <v-row>
      <v-col v-for="service in services" :key="`${service.title}`">
        <v-dialog
        v-model="dialog"
        width="500"
        >
        <template v-slot:activator="{ on, attrs }">
          <v-card
            v-bind="attrs"
            v-on="on"
            flat
          >
            <v-img
              src="https://picsum.photos/350/165?random"
              height="400px"
              class="grey darken-4"
            >
              <v-card-title class="title">
                {{ service.title }}
              </v-card-title>
            </v-img>
          </v-card>
        </template>
        <v-card>
          <v-card-title class="headline grey lighten-2">
            {{ service.title }}
          </v-card-title>
          <v-card-text>
            {{ service.description }}
          </v-card-text>
          <v-divider></v-divider>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="primary"
              text
              @click="dialog = false"
            >
              cerrar
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'Service',
  data: () => ({
    dialog: false,
    services: [
      {
        title: "Tasaciones",
        description: "Una buena tasación requiere de la correcta aplicación de las distintas técnicas que forman la actividad de tasar una propiedad, por eso queremos informarte que contamos con la formación profesional y académica necesaria para justipreciar un inmueble.  Realiza tu consulta sin cargo para mayor información, nosotros te ayudamos."
      },
      {
        title: "Loteos",
        description: "Contamos con experiencia dentro de la inmobiliaria para el manejo y administración de venta de tierras a gran escala, con distintas formas de aplicación según varíe el método de pago.  Tenemos a disposición los profesionales necesarios para llevar a cabo el trabajo que implica el desarrollo de un loteo.  Realiza tu consulta sin cargo para mayor información, nosotros te ayudamos."
      },
      {
        title: "Consorcios",
        description: "Nuestra administración de consorcios cuenta con el soporte en software para el pago de las expensas y gastos que la figura del consorcio demande, como así también una atención especializada para toda situación que sea necesaria la intervención de la administración.  Realiza tu consulta sin cargo para mayor información, nosotros te ayudamos."
      },
    ],
  })
}
</script>
