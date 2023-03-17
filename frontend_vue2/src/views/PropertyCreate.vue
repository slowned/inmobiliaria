<template>
  <v-container>
    <v-form>

      <v-row>
        <v-file-input
          label="Fotos"
          filled
          prepend-icon="mdi-camera"
          @change="onPhotoSelected"
        ></v-file-input>
      </v-row>



      <v-row>

        <v-col>
          <v-text-field v-model="address" label="Direccion"></v-text-field>
        </v-col>
        <v-col>
          <v-text-field v-model="expensas" label="Expensas"></v-text-field>
        </v-col>

        <v-col>
          <v-select
            v-model="home_type"
            :items="homeType"
            label="Tipo Inmueble"
          ></v-select>
        </v-col>

      </v-row>


      <!--
        <v-col>
          <v-text-field 
            required
            :rules="[() => !!amount || 'campo requerido']"
            v-model="amount" label="Precio"></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-text-field v-model="rooms" label="Cantidad de Ambientes"></v-text-field>
        </v-col>
        <v-col>
          <v-text-field v-model="bedroom" label="Cantidad de Dormitorios"></v-text-field>
        </v-col>
        <v-col>
          <v-text-field v-model="bathroom" label="Cantidad de Baños"></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-select
            v-model="state"
            :items="homeStates"
            label="Estado"
          ></v-select>
        </v-col>
        <v-col>
          <v-text-field v-model="services" label="Servicios"></v-text-field>
        </v-col>
        <v-col>
          <v-select
            v-model="garage"
            :items="siNo"
            label="Tiene Garage"
          ></v-select>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-text-field v-model="ages" label="Antiguedad"></v-text-field>
        </v-col>
        <v-col>
          <v-text-field v-model="total_surface" label="Superficie Total"></v-text-field>
        </v-col>
        <v-col>
          <v-text-field v-model="coordinates" label="Coordenadas"></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-textarea
            v-model="description"
            label="Descripcion"
            auto-grow
            outlined
            rows="3"
            row-height="25"
            shaped
          ></v-textarea>
        </v-col>
      </v-row>
      -->

      <v-btn class="mr-4" @click="submit">Crear</v-btn>
    </v-form>
  </v-container>
</template>
<script>
// import { HOME_TYPE, HOME_STATES, SI_NO } from "@/constants.js"
import { HOME_TYPE } from "@/constants.js"
import PropertyService from "@/services/PropertyService.js";

export default {
  name: 'createForm',
  data() {
    return {
      homeType: HOME_TYPE,
      /* homeStates: HOME_STATES, */
      /* siNo: SI_NO, */
      selectedPhoto: null,
      /* amount: '', */
      /* ages: '', */
      address: '',
      expensas: '',
      /* bathroom: '', */
      /* bedroom: '', */
      /* coordinates: '', */
      /* description: '', */
      /* garage: '', */
      home_type: '',
      /* rooms: '', */
      /* total_surface: '', */
      /* state: '', */
      /* services: '', */
      files: [],
      /* statesOptions: { */
      /*   'exelente': 0, */
      /*   'muy bueno': 1, */
      /*   'bueno': 2, */
      /*   'reparar': 3, */
      /* } */
    }
  },
  methods: {
    onPhotoSelected(image) {
      this.selectedPhoto = image;
      this.files.push(image);
    },
    formatHomeType() {
      let d = {
        'casa': 0,
        'departamento': 1,
        'PH': 2,
        'duplex': 3,
      }
      return d[this.home_type]
    },
    formatHomeState() {
      return this.statesOptions[this.state]
    },
    formatGarage() {
      let d = {
        'NO': 0,
        'SI': 1,
      }
      return d[this.garage]
    },
    getParams() {
      var formData = new FormData();
      for(let i = 0; i < this.files.length; i++) {
        let file = this.files[i];
        formData.append(`images[]`, file);
      }

      formData.append("address", this.address);
      formData.append("expensas", this.expensas);
      formData.append("home_type", this.formatHomeType());
      // formData.append("amount", this.amount);
      // formData.append("ages", this.ages);
      // formData.append("bathroom", this.bathroom);
      // formData.append("coordinates", this.coordinates);
      // formData.append("description", this.description);
      // formData.append("garage", this.formatGarage());
      // formData.append("rooms", this.rooms);
      // formData.append("total_surface", this.total_surface);
      // formData.append("state", this.formatHomeState());
      // formData.append("services", this.services);
      return formData

      //return {
      //  image: this.selectedPhoto, // cambiar a files para manejar multiples imagenes
      //  amount: this.amount,
      //  ages: this.ages,
      //  address: this.address,
      //  bathroom: this.bathroom,
      //  bedroom: this.bedroom,
      //  coordinates: this.coordinates,
      //  description: this.description,
      //  garage: this.formatGarage(),
      //  home_type: this.formatHomeType(),
      //  rooms: this.rooms,
      //  total_surface: this.total_surface,
      //  state: this.formatHomeState(),
      //  services: this.services,
      //}
    },
    submit() {
      let params = this.getParams();

      PropertyService.createProperty(params)
        .then((response) => {
          console.log('created', response.status);
        })
        .catch((error) => {
          console.log(error)
        });
    },
  },
}
</script>
