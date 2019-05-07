<template>
    <v-container fluid>
        <v-layout>
            <v-flex xs10>
                <v-card>
                    <v-card-title>
                        <div>
                            <div class="headline">
                                {{ dadosEspecie.nomes_populares }}
                            </div>
                            <span class="font-italic">
                                {{ dadosEspecie.nome_cientifico }} / {{ dadosEspecie.familia }}
                            </span>
                        </div>
                    </v-card-title>
                    <v-list>
                        <v-list-tile v-if="dadosEspecie.inicio_colheita !== ''">
                            <v-icon class="pa-2">
                                access_alarm
                            </v-icon>
                            Início da colheita: {{ dadosEspecie.inicio_colheita }} dias
                        </v-list-tile>
                        <v-list-tile v-if="dadosEspecie.porte !== ''">
                            <v-icon class="pa-2">
                                toys
                            </v-icon>
                            Porte:
                            <span
                                v-html="dadosEspecie.porte"
                                class="pl-2"
                            />
                        </v-list-tile>
                        <v-list-tile v-if="dadosEspecie.sucessao !== ''">
                            <v-icon class="pa-2">
                                trending_up
                            </v-icon>
                            Sucessão:
                            <span
                                v-html="dadosEspecie.sucessao"
                                class="pl-2"
                            />
                        </v-list-tile>
                        <v-list-tile v-if="dadosEspecie.temperatura_min !== ''">
                            <v-icon class="pa-2">
                                brightness_low
                            </v-icon>
                            Temperatura: 
                            <span
                                v-html="dadosEspecie.temperatura_min"
                                class="pl-2"
                            />ºC - <span v-html="dadosEspecie.temperatura_max"/>ºC
                        </v-list-tile>
                    </v-list>
                    <v-card-actions>
                        <v-btn
                            class="green lighten-1"
                        >
                            <v-icon
                                white
                            >
                                edit
                            </v-icon>
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';

export default {
    name: 'VisualizarEspecie',
    created() {
        if (typeof this.$route.params.id !== 'undefined') {
            this.buscarEspecie(this.$route.params.id);
        }
    },
    methods: {
        ...mapActions({
            buscarEspecie: 'especie/buscarEspecie',
        }),
    },
    computed: {
        ...mapGetters({
            dadosEspecie: 'especie/especie',
        }),
    },
};
</script>
