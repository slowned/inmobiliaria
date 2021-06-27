<template>
  <v-container>
    <v-form>
        'images',
      <v-row>
        <v-col>
          <v-text-field v-model="amount" label="Precio"></v-text-field>
        </v-col>
        <v-col>
          <v-text-field v-model="ages" label="Antiguedad"></v-text-field>
        </v-col>
        <v-col>
          <v-text-field v-model="address" label="Direccion"></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-text-field v-model="bathroom" label="Cantidad de Baños"></v-text-field>
        </v-col>
        <v-col>
          <v-text-field v-model="bedroom" label="Cantidad de Dormitorios"></v-text-field>
        </v-col>
        <v-col>
          <v-text-field v-model="coordinates" label="Coordenadas"></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-text-field v-model="description" label="Descripcion"></v-text-field>
        </v-col>
        <v-col>
          <v-text-field v-model="garage" label="tiene Garage"></v-text-field>
        </v-col>
        <v-col>
          <v-select
            v-model="home_type"
            :items="homeType"
            label="Tipo Inmueble"
          ></v-select>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-text-field v-model="rooms" label="Cantidad de Ambientes"></v-text-field>
        </v-col>
        <v-col>
          <v-text-field v-model="total_surface" label="Superficie Total"></v-text-field>
        </v-col>
        <v-col>
          <v-text-field v-model="state" label="Estado"></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-text-field v-model="services" label="Servicios"></v-text-field>
        </v-col>
      </v-row>
        <v-btn class="mr-4" @click="submit">Crear</v-btn>
    </v-form>
  </v-container>
</template>
<script>
import HOME_TYPE from "@/constants.js"
import PropertyService from "@/services/PropertyService.js";

export default {
  name: 'createForm',
  data() {
    return {
      homeType: HOME_TYPE,
      images_set: [],
      amount: '',
      ages: '',
      address: '',
      bathroom: '',
      bedroom: '',
      coordinates: '',
      description: '',
      garage: '',
      home_type: '',
      rooms: '',
      total_surface: '',
      state: '',
      services: '',
    }
  },
  methods: {
    get_params() {
      return {}
    },
    submit() {
      PropertyService.creteProperty(this.get_params)
        .then((response) => {
          console.log('created', response.status);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
}
</script>
