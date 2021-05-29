<template>
  <v-container>
    <v-row>
      <v-col cols="4">
        <v-dialog
          v-model="dialog"
          width="500"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-card
              v-bind="attrs"
              v-on="on"
            >
              <v-img
                src="https://picsum.photos/350/165?random"
                height="125"
                class="grey darken-4"
              ></v-img>
              <v-card-title class="title">
                TASACIONES
              </v-card-title>
            </v-card>
          </template>

          <v-card>
            <v-card-title class="headline grey lighten-2">
              Tasaciones
            </v-card-title>

            <v-card-text>
              Una buena tasación requiere de la correcta aplicación de las distintas técnicas que forman la actividad de tasar una propiedad, por eso queremos informarte que contamos con la formación profesional y académica necesaria para justipreciar un inmueble.
              Realiza tu consulta sin cargo para mayor información, nosotros te ayudamos.
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
      <v-col cols="4">
        <v-card>
          <v-img
            src="https://picsum.photos/350/165?random"
            height="125"
            class="grey darken-4"
          ></v-img>
          <v-card-title class="title">
            LOTEOS
          </v-card-title>
        </v-card>
      </v-col>
      <v-col cols="4">
        <v-card>
          <v-img
            src="https://picsum.photos/350/165?random"
            height="125"
            class="grey darken-4"
          ></v-img>
          <v-card-title class="title">
            CONSORCIOS
          </v-card-title>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'Service',
  data: () => ({
    dialog: false,
  })
}
</script>
