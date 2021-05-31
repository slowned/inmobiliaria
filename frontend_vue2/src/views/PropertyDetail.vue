<template>
  <v-main>
      <v-container>
        <v-row>
          <v-col cols="8">
            <v-carousel>
              <v-carousel-item
              v-for="(item,i) in imgs"
              :key="i"
              :src="item.src"
              reverse-transition="fade-transition"
              transition="fade-transition"
              ></v-carousel-item>
            </v-carousel>
          </v-col>
          <v-col cols="4">
            <v-data-iterator
              :items="items"
              :items-per-page.sync="itemsPerPage"
              hide-default-footer
            >
              <template v-slot:default="props">
                <v-row>
                  <v-col
                    v-for="item in props.items"
                    :key="item.name"
                    cols="12"
                  >
                    <v-card>
                      <v-card-title class="subheading font-weight-bold">
                        {{ item.name }}
                      </v-card-title>

                      <v-divider></v-divider>

                      <v-list dense>
                        <v-list-item>
                          <v-list-item-content>Superficie total:</v-list-item-content>
                          <v-list-item-content class="align-end">
                            {{ item.calories }}
                          </v-list-item-content>
                        </v-list-item>

                        <v-list-item>
                          <v-list-item-content>Superficie cubierta:</v-list-item-content>
                          <v-list-item-content class="align-end">
                            {{ item.fat }}
                          </v-list-item-content>
                        </v-list-item>

                        <v-list-item>
                          <v-list-item-content>Habitaciones:</v-list-item-content>
                          <v-list-item-content class="align-end">
                            {{ item.carbs }}
                          </v-list-item-content>
                        </v-list-item>

                        <v-list-item>
                          <v-list-item-content>Banios:</v-list-item-content>
                          <v-list-item-content class="align-end">
                            {{ item.protein }}
                          </v-list-item-content>
                        </v-list-item>

                        <v-list-item>
                          <v-list-item-content>Ambientes:</v-list-item-content>
                          <v-list-item-content class="align-end">
                            {{ item.sodium }}
                          </v-list-item-content>
                        </v-list-item>

                        <v-list-item>
                          <v-list-item-content>Antiguedad:</v-list-item-content>
                          <v-list-item-content class="align-end">
                            {{ item.calcium }}
                          </v-list-item-content>
                        </v-list-item>

                      </v-list>
                    </v-card>
                  </v-col>
                </v-row>
              </template>

            </v-data-iterator>
          </v-col>
        </v-row>

        <v-row>
          <v-card flat>
            <v-card-title>Detalles del inmueble</v-card-title>
            <v-card-text>
              Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
            </v-card-text>
            <v-card-text>
              Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
            </v-card-text>
          </v-card>
        </v-row>
    <v-row justify="center">
      <v-card flat width="100%">
        <v-card-title>Ubicacion</v-card-title>
        <div class="">
          <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6542.854006400544!2d-57.95772883221242!3d-34.920826461263566!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95a2e62b1f0085a1%3A0xbcfc44f0547312e3!2sLa%20Plata%2C%20Buenos%20Aires%20Province%2C%20Argentina!5e0!3m2!1sen!2suk!4v1622406892309!5m2!1sen!2suk" width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
        </div>
      </v-card>
    </v-row>
  </v-container>

  </v-main>
</template>

<script>
export default {
  name: "Contact",
  data () {
    return {
      imgs: [
        {
          src: 'https://i.pinimg.com/originals/b6/33/b5/b633b526ec5a84c0313cf553d85bcddf.jpg',
        },
        {
          src: 'https://www.arkiplus.com/wp-content/uploads/2020/08/dise%C3%B1os-casas-sencillas.jpg',
        },
        {
          src: 'https://cf.bstatic.com/images/hotel/max1024x768/120/120360227.jpg',
        },
        {
          src: 'https://www.lincolninst.edu/sites/default/files/styles/issue_feature/public/sources/articles/stigma-to-housing-fix-lla180102-highlight-b.jpg?itok=LlOafTaG',
        },
      ],
      itemsPerPage: 1,
      items: [
        {
          name: 'Detalles',
          calories: 159,
          fat: 6.0,
          carbs: 24,
          protein: 4.0,
          sodium: 87,
          calcium: '14%',
          iron: '1%',
        },
      ],
    }
  },


};
</script>

<style>

</style>






<!-- <template>
  <div v-if="property">
    <h3>Detalle de la propiedad</h3>
    <span>Direccion {{property.address}}</span>
    <span>Precio ${{property.price}}</span>
    <span>Descripcion: {{property.description}}</span>
  </div>
</template>

<script>

import PropertyService from "@/services/PropertyService.js"

export default {
  props: ['id'],
  data() {
    return {
      property: null
    }
  },
  created() {
    PropertyService.getProperty(this.id)
      .then((response) => {
        this.property = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>

<style>
</style> -->
