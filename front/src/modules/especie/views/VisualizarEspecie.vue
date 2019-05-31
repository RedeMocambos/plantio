<template>
    <v-container fluid>
        <v-layout>
            <v-flex
                xs10
                offset-xs1
            >
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
                            <v-icon
                                class="pa-2"
                                color="green darken-3"
                            >
                                local_florist
                            </v-icon>
                            Início da colheita: {{ dadosEspecie.inicio_colheita }} dias
                        </v-list-tile>
                        <v-list-tile v-if="dadosEspecie.porte !== ''">
                            <v-icon
                                class="pa-2"
                                color="green darken-3"
                            >
                                nature
                            </v-icon>
                            Porte:
                            <span
                                class="pl-2"
                                v-html="dadosEspecie.porte"
                            />
                        </v-list-tile>
                        <v-list-tile v-if="dadosEspecie.sucessao !== ''">
                            <v-icon
                                class="pa-2"
                                color="green darken-3"
                            >
                                nature
                            </v-icon>
                            Sucessão:
                            <span
                                class="pl-2"
                                v-html="dadosEspecie.sucessao"
                            />
                        </v-list-tile>
                        <v-list-tile v-if="dadosEspecie.temperatura_min !== ''">
                            <v-icon
                                class="pa-2"
                                color="green darken-3"
                            >
                                brightness_low
                            </v-icon>
                            Temperatura:
                            <span
                                class="pl-2"
                                v-html="dadosEspecie.temperatura_min"
                            />ºC - <span v-html="dadosEspecie.temperatura_max"/>ºC
                        </v-list-tile>
                        <v-list-tile v-if="dadosEspecie.tempo_vida !== ''">
                            <v-icon
                                class="pa-2"
                                color="green darken-3"
                            >
                                query_builder
                            </v-icon>
                            Tempo de vida:
                            <span
                                class="pl-2"
                                v-html="dadosEspecie.tempo_vida"
                            />
                        </v-list-tile>
                        <v-list-tile v-if="dadosEspecie.umidade !== ''">
                            <v-icon
                                class="pa-2"
                                color="green darken-3"
                            >
                                format_color_fill
                            </v-icon>
                            Umidade:
                            <span
                                class="pl-2"
                                v-html="dadosEspecie.umidade"
                            />
                        </v-list-tile>
                        <v-list-tile v-if="dadosEspecie.exigencia_solo !== ''">
                            <v-icon
                                class="pa-2"
                                color="green darken-3"
                            >

                                open_with
                            </v-icon>
                            Exigência de solo:
                            <span
                                class="pl-2"
                                v-html="dadosEspecie.exigencia_solo"
                            />
                        </v-list-tile>
                        <v-list-tile v-if="dadosEspecie.tolerancia_poda !== ''">
                            <v-icon
                                class="pa-2"
                                color="green darken-3"
                            >
                                build
                            </v-icon>
                            Tolerância a poda:
                            <span
                                class="pl-2"
                                v-html="dadosEspecie.tolerancia_poda"
                            />
                        </v-list-tile>
                        <v-list-tile v-if="dadosEspecie.estrato !== ''">
                            <v-icon
                                class="pa-2"
                                color="green darken-3"
                            >
                                nature
                            </v-icon>
                            Estrato:
                            <span
                                class="pl-2"
                                v-html="dadosEspecie.estrato"
                            />
                        </v-list-tile>
                    </v-list>
                    <v-card-actions>
                        <v-btn
                            class="green lighten-1"
                            @click="abrirEdicao()"
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
    computed: {
        ...mapGetters({
            dadosEspecie: 'especie/especie',
        }),
        id() {
            return this.$route.params.id;
        },
    },
    created() {
        if (typeof this.$route.params.id !== 'undefined') {
            this.buscarEspecie(this.$route.params.id);
        }
    },
    methods: {
        ...mapActions({
            buscarEspecie: 'especie/buscarEspecie',
        }),
        abrirEdicao() {
            const path = `/especie/${this.id}/editar`;
            this.$router.push({ path });
        },
    },
};
</script>
