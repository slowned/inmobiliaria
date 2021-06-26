<template>
  <div>
    <v-spacer> </v-spacer>
    <v-footer
      padless

      dark
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
              <v-avatar size="100">
                <img
                  src="https://cdn.vuetifyjs.com/images/john.jpg"
                  alt="John"
                >
              </v-avatar>
              FIRMA O MATRICULA
            </v-col>
            <v-col>
              <v-avatar size="100">
                <img
                  src="https://cdn.vuetifyjs.com/images/john.jpg"
                  alt="John"
                >
              </v-avatar>
              FIRMA O MATRICULA
            </v-col>
          </v-row>
        </v-container>

        <v-divider></v-divider>

        <v-card-text class="white--text">
          telefono: 345-129391
          <v-spacer> </v-spacer>
          email: inmo@test.com
        </v-card-text>
      </V-CARD>
    </V-FOOTER>
    </div>
</template>

<script>
  export default {
    data: () => ({
      icons: [
        'mdi-facebook',
        'mdi-twitter',
        'mdi-linkedin',
        'mdi-instagram',
      ],
    }),
  }
</script>
