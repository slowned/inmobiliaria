<template>
  <v-container>
    <v-card flat>
      <v-card-title>ALQUILERES</v-card-title>
      <v-card-text> Para el sector Alquileres, nuestra inmobiliaria cuenta con varias formas de publicitar y comercializar las propiedades en situación de locación.
        Contamos con una propia página web como así también redes sociales; Instagram y Facebook.
        Creemos necesaria la utilización de otras plataformas de renombre que nos van a brindar la posibilidad de hacer crecer la cantidad de veedores de las propiedades ofrecidas, y así también cubrir las demandas actuales, que casi en su totalidad se manifiestan por internet.
        Nuestros valores de vanguardia nos acercan a la era digital para evitar el uso del papel y así contribuir con el medio ambiente.
        Realiza tu consulta sin cargo para mayor información, nosotros te ayudamos.</v-card-text>
    </v-card>
    <v-row justify="end">
      <v-col
        cols="6"
        sm="3"
      >
        <v-select
            :items="order"
            label="Ordenar por"
            dense
          ></v-select>
      </v-col>
    </v-row>
    <v-row>
      <v-dialog
        v-model="dialog"
        max-width="600px"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            color="#846D34"
            dark
            right
            fixed
            fab
            v-bind="attrs"
            v-on="on"
          >
            <v-icon>mdi-magnify</v-icon>
          </v-btn>
        </template>
          <SearchForm />
      </v-dialog>
    </v-row>
    <v-row>
        <v-row>
          <v-col cols="12" md="4" sm="6" v-for="property in properties" :key="property.id">
            <PropertyList :property="property" />
          </v-col>
        </v-row>
    </v-row>

  </v-container>
</template>

<script>
import PropertyList from "@/components/PropertyList.vue";
import SearchForm from "@/components/SearchForm";
import PropertyService from "@/services/PropertyService.js";

export default {
  name: "Properties",
  components: {
    PropertyList,
    SearchForm,
  },
  data() {
    return {
      properties: null,
      dialog: false,
      order: ['Mas caro', 'Mas barato', 'Publicacion mas reciente', 'Publicacion mas antigua'],
    };
  },
  created() {
    PropertyService.getProperties()
      .then((response) => {
        this.properties = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
  methods: {
    filterProperties(queryParams) {
      console.log('lo params viteh', queryParams);
      PropertyService.filterProperties(queryParams)
        .then((response) => {
          this.properties = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    reset() {
      this.$refs.form.reset()
    },

  },
};
</script>

<style scoped>
* {
  font-family: DIN pro;
}
</style>
